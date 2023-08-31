<template>
  <div class="class_plan_analyse">

    <div class="class_data_sideBar">

      <el-button class="analyse_side_btn" @click="changeThePage(1)">课程数据</el-button>
      <el-button class="analyse_side_btn" @click="changeThePage(2)">课程完成度</el-button>

      <div class="data_select">
        年份：
        <el-select v-model="selectedYear" placeholder="所有" size="large">
          <el-option v-for="item in years" :key="item" :value="item" @click="clickYear()" />
        </el-select>
      </div>

      <div class="data_select" v-if="this.changeNum == 2">
        课程：
        <el-select v-model="selectedLesson" placeholder="所有" size="large" no-data-text="暂无数据">
          <el-option v-for="item in lessons" :key="item" :value="item" @click="clickLesson()" />
        </el-select>
      </div>
    </div>

    <div v-if="this.changeNum == 1">

      <el-table :data="nowLesson" style="width: 95%; font-size: 18px; margin-left: 30px" max-height="650" size="large"
        empty-text="暂无数据">
        <el-table-column prop="name" label="课程" />
        <el-table-column prop="year" label="年份" />
        <el-table-column fixed="right" label="操作">
          <template #default="scope">
            <el-button link type="success" size="large" @click="homeworkClick(scope.row)">
              作业
            </el-button>

            <el-button link type="primary" size="large" @click="examClick(scope.row)">
              考试
            </el-button>

            <el-button link type="danger" size="large" @click="experimentClick(scope.row)">
              实验
            </el-button>

          </template>
        </el-table-column>
      </el-table>

      <el-dialog title="上传文件" v-model="homeworkVisible" width="30%" center="true" :close-on-click-modal="false"
        :close-on-press-escape="false" :show-close="false">
        <el-button class="dialog_btn" type="primary" @click="homeworkExample">下载模板文件</el-button>
        <el-upload action="" :on-change="homeworkChange">
          <el-button type="success">
            上传作业
          </el-button>
        </el-upload>
        <template #footer>
          <el-button @click="homeworkSure">确 定</el-button>
          <el-button @click="homeworkCancel">取 消</el-button>
        </template>
      </el-dialog>

      <el-dialog title="上传文件" v-model="examVisible" width="30%" center="true" :close-on-click-modal="false"
        :close-on-press-escape="false" :show-close="false">
        <el-button class="dialog_btn" type="primary" @click="examExample">下载模板文件</el-button>
        <el-upload action="" :on-change="examChange">
          <el-button type="success">
            上传考试
          </el-button>
        </el-upload>
        <template #footer>
          <el-button @click="examSure">确 定</el-button>
          <el-button @click="examCancel">取 消</el-button>
        </template>
      </el-dialog>

      <el-dialog title="上传文件" v-model="experimentVisible" width="30%" center="true" :close-on-click-modal="false"
        :close-on-press-escape="false" :show-close="false">
        <el-button class="dialog_btn" type="primary" @click="experimentExample">下载模板文件</el-button>
        <el-upload action="" :on-change="experimentChange">
          <el-button type="success">
            上传实验
          </el-button>
        </el-upload>
        <template #footer>
          <el-button @click="experimentSure">确 定</el-button>
          <el-button @click="experimentCancel">取 消</el-button>
        </template>
      </el-dialog>

    </div>

    <div v-else-if="this.changeNum == 2" class="course_completion">
      <el-button @click="calculateCompletion(this.selectedYear, this.selectedLesson)">计算完成度</el-button>
      <el-table :data="tableDataCourseCompletion" :span-method="objectSpanMethod" border
        :header-cell-style="{ 'text-align': 'center' }" :cell-style="{ 'text-align': 'center' }"
        style="width:fit-content;margin-top:15px;" max-height="600px" empty-text="暂无数据">
        <el-table-column prop="graduationPoints" label="毕业指标点" width="100px" />
        <el-table-column prop="courseWeights" label="课程达成目标值" width="130px" />
        <el-table-column prop="courseScores" label="课程达成实际值" width="130px" />
        <el-table-column prop="courseGoals" label="课程目标" width="100px" />
        <el-table-column prop="courseGoalWeights" label="课程目标达成目标值" width="160px" />
        <el-table-column prop="courseGoalScores" label="课程目标达成实际值" width="160px" />
        <el-table-column prop="assessMethodWeightForHomework" label="作业权重" width="100px" />
        <el-table-column prop="assessMethodWeightForExam" label="考试权重" width="100px" />
        <el-table-column prop="assessMethodWeightForExperience" label="实验权重" width="100px" />
        <el-table-column prop="courseGoalPercent" label="课程目标达成度" width="130px" />
      </el-table>
    </div>
  </div>
</template>

<script>

import { ElSelect } from 'element-plus'
import { ElTable } from 'element-plus'
import { ElButton } from 'element-plus'
import { ElUpload } from 'element-plus'
import { ElDialog } from 'element-plus'
import * as XLSX from 'xlsx'
import { getTarget, getWeight, getRatio, getMine, uploadData, getData, uploadGoal } from '../api/api.js'

export default {
  inject: ['globalData'],
  name: 'ClassPlanAnalyse',
  components: {
    ElSelect,
    ElButton,
    ElTable,
    ElUpload,
    ElDialog,
  },

  data() {
    return {
      changeNum: 1,

      // 上面为数据上传所用数据
      homeworkVisible: false,
      examVisible: false,
      experimentVisible: false,
      name: [],
      score: [],
      uploadLesson: '',
      uploadYear: '',
      selectedYear: 'all',
      years: ["all",],
      selectedLesson: '',
      lessons: [],
      nowLesson: [],
      fosterLesson: [],

      //单门课程所对应指标点及权重
      weights: {
        // '1-1':'0.5',
        // '1-2':'0.7'
      },

      //单元格合并
      spanArr: [], // 一个空的数组，用于存放每一行记录的合并数
      pos: 0, // spanArr 的索引

      tableDataCourseCompletion: [
        // {
        //   graduationPoints: '1.1 完成xxx',//毕业指标点
        //   courseWeights: '0.1',//课程达成目标值
        //   courseScores: '0.3',//课程达成实际值(计算)
        //   courseGoals: '1.xxx',//课程目标
        //   courseGoalWeights: '0.1',//课程目标达成目标值
        //   courseGoalScores: '0.2',//课程目标达成实际值(计算)
        //   assessMethodWeightForHomework: '0.1',
        //   assessMethodWeightForExam: '0.5',
        //   assessMethodWeightForExperience: '0.4',
        //   courseGoalPercent: '85.6%',//课程目标达成度(计算)
        // },
      ],
    }
  },

  created() {

  },

  mounted() {
    this.getFosterLesson()
  },

  methods: {
    changeThePage(num) {
      this.changeNum = num;
    },

    //获取课程完成度分析所需数据
    getDataForCourseCompletion(selectedYear, selectedLesson) {
      // {
      //   graduationPoints: '1.1 完成xxx',//毕业指标点
      //   courseWeights: '0.1',//课程达成目标值
      //   courseScores: '0.3',//课程达成实际值(计算)
      //   courseGoals: '1.xxx',//课程目标
      //   courseGoalWeights: '0.1',//课程目标达成目标值
      //   courseGoalScores: '0.2',//课程目标达成实际值(计算)
      //   assessMethods: '实验',//评价方式
      //   assessMethodWeights: '20%',//权重
      //   courseGoalPercent: '85.6%',//课程目标达成度(计算)
      // },
      getTarget(selectedYear, selectedLesson).then(response => {
        console.log("获取课程目标对指标点权重");
        console.log(response.data);
        this.tableDataCourseCompletion.length = 0
        for (var i = 0; i < response.data.content.length; i++) {
          var data = response.data.content[i];
          this.tableDataCourseCompletion.push(
            {
              graduationPoints: data.pointIndex,//当前是序号，需要加上内容
              courseWeights: '0',//课程达成目标值
              courseScores: '0',//课程达成实际值(计算)
              courseGoals: data.classTargetIndex,//当前是序号，需要加上内容
              courseGoalWeights: data.weight,
              courseGoalScores: '0',//课程目标达成实际值(计算)
              assessMethodWeightForHomework: '0',
              assessMethodWeightForExam: '0',
              assessMethodWeightForExperience: '0',
              courseGoalPercent: '0',//课程目标达成度(计算)
            }
          )
        }

        //对课程完成度分析表中数据进行排序
        for (var j = 0; j < this.tableDataCourseCompletion.length; j++) {
          for (i = 0; i < this.tableDataCourseCompletion.length - 1; i++) {
            let item1 = this.tableDataCourseCompletion[i]
            let item2 = this.tableDataCourseCompletion[i + 1]
            let count1 = Number(item1.graduationPoints.charAt(0)) * 100 + Number(item1.graduationPoints.charAt(2)) * 10 + Number(item1.courseGoals)
            let count2 = Number(item2.graduationPoints.charAt(0)) * 100 + Number(item2.graduationPoints.charAt(2)) * 10 + Number(item2.courseGoals)
            if (count1 > count2) {
              this.tableDataCourseCompletion[i] = this.tableDataCourseCompletion.splice(i + 1, 1, this.tableDataCourseCompletion[i])[0]
            }
          }
        }

        this.getList();

        getWeight(selectedYear, selectedLesson).then(response => {
          console.log("获取课程对指标点权重");
          console.log(response.data);
          this.weights = {}
          for (var i = 0; i < response.data.content.length; i++) {
            var item = response.data.content[i]
            var newProperty = item.pointIndex
            this.weights[newProperty] = item.weight
          }
          for (let key in this.tableDataCourseCompletion) {
            this.tableDataCourseCompletion[key].courseWeights = this.weights[this.tableDataCourseCompletion[key].graduationPoints]
          }
        })

        getRatio(selectedYear, selectedLesson).then(response => {
          console.log("获取每个课程目标的考核方式权重");
          console.log(response.data);
          for (let key in this.tableDataCourseCompletion) {
            for (var i = 0; i < response.data.content.length; i++) {
              var item = response.data.content[i]
              if (this.tableDataCourseCompletion[key].courseGoals == item.classTargetIndex) {
                this.tableDataCourseCompletion[key].assessMethodWeightForHomework = item.homeworkRatio
                this.tableDataCourseCompletion[key].assessMethodWeightForExam = item.examRatio
                this.tableDataCourseCompletion[key].assessMethodWeightForExperience = item.experienceRatio
                break;
              }
            }
          }
        })
      })
    },

    calculateCompletion(selectedYear, selectedLesson) {
      if (selectedLesson == "请选择年份") {
        this.$message.error("请选择课程");
      }
      else {
        getData(selectedLesson, selectedYear).then(response => {
          console.log("获取当前课程考核数据");
          console.log(response.data);

          if (response.data.code == 'false') {
            this.$message.error('当前课程未上传成绩数据')
          } else {

            for (let key in this.tableDataCourseCompletion) {
              let count = this.tableDataCourseCompletion[key].assessMethodWeightForHomework * response.data.content[0].homework
                + this.tableDataCourseCompletion[key].assessMethodWeightForExam * response.data.content[0].exam
                + this.tableDataCourseCompletion[key].assessMethodWeightForExperience * response.data.content[0].experience
              count = (Math.round(count * 100)) / 100
              //计算课程目标达成度
              this.tableDataCourseCompletion[key].courseGoalPercent = count + '%'

              //计算课程目标达成实际值
              this.tableDataCourseCompletion[key].courseGoalScores = (Math.round(count * this.tableDataCourseCompletion[key].courseGoalWeights * 10)) / 1000
            }

            //计算课程达成实际值
            var completion = {};
            for (let key in this.tableDataCourseCompletion) {
              if (!(this.tableDataCourseCompletion[key].graduationPoints in completion)) {
                completion[this.tableDataCourseCompletion[key].graduationPoints] = 0
              }
              completion[this.tableDataCourseCompletion[key].graduationPoints] +=
                (Math.round(this.tableDataCourseCompletion[key].courseWeights * this.tableDataCourseCompletion[key].courseGoalScores * 1000)) / 1000
            }
            for (let key in this.tableDataCourseCompletion) {
              this.tableDataCourseCompletion[key].courseScores = completion[this.tableDataCourseCompletion[key].graduationPoints]
            }

            //将课程达成实际值上传到后端
            for (let key in completion) {
              uploadGoal(selectedYear, selectedLesson, key, completion[key]).then(response => {
                console.log(response.data);
              })
            }
          }
        })
      }
    },

    //将表格合并应用到表格上
    // eslint-disable-next-line
    objectSpanMethod({ row, column, rowIndex, columnIndex }) {
      if (columnIndex === 0 || columnIndex === 1 || columnIndex === 2) {
        const _row = this.spanArr[rowIndex];
        const _col = _row > 0 ? 1 : 0;
        return {
          rowspan: _row,
          colspan: _col
        };
      }
    },

    // 根据表格数据设置单元格合并的规律
    getList() {
      // 设定一个数组spanArr/contentSpanArr来存放要合并的格数，同时还要设定一个变量pos/position来记录
      this.spanArr = [];
      for (var i = 0; i < this.tableDataCourseCompletion.length; i++) {
        if (i === 0) {
          this.spanArr.push(1);
          this.pos = 0;
        } else {
          if (this.tableDataCourseCompletion[i].graduationPoints === this.tableDataCourseCompletion[i - 1].graduationPoints) {
            this.spanArr[this.pos] += 1;
            this.spanArr.push(0);
          } else {
            this.spanArr.push(1);
            this.pos = i;
          }
        }
      }
    },

    //下面为数据上传页面函数
    clickYear() {
      this.nowLesson = []
      if (this.selectedYear === 'all') {
        this.selectedLesson = "请选择年份"
        for (let item in this.fosterLesson) {
          this.nowLesson.push(this.fosterLesson[item])
        }
      } else {
        this.selectedLesson = "请选择课程"
        for (let item in this.fosterLesson) {
          if (this.fosterLesson[item].year === this.selectedYear) {
            this.nowLesson.push(this.fosterLesson[item])
          }
        }
      }
      this.getLesson()
    },

    clickLesson() {
      this.getDataForCourseCompletion(this.selectedYear, this.selectedLesson)
    },

    getLesson() {
      this.lessons = []
      if (this.selectedYear !== 'all') {
        for (let item in this.nowLesson) {
          if (this.lessons.indexOf(this.nowLesson[item].name) === -1) {
            this.lessons.push(this.nowLesson[item].name)
          }
        }
      }
    },

    getYear() {
      let temp = []
      for (let item in this.fosterLesson) {
        if (temp.indexOf(this.fosterLesson[item].year) === -1) {
          temp.push(this.fosterLesson[item].year)
        }
      }
      temp.sort()
      for (let i = 0; i < temp.length; i++) {
        this.years.push(temp[i])
      }
    },

    getFosterLesson() {
      //从数据库获取所有方案的ID、facility、subject、year
      // let getLesson = [
      //   {
      //     name: "数据库原理",
      //     year: "2020",
      //   },
      // ]
      let userAccount = this.globalData.account
      getMine(userAccount).then(response => {
        let getLesson = []
        for (let i in response.data.content) {
          let dict = {}
          dict.name = response.data.content[i].className
          dict.year = response.data.content[i].year
          getLesson.push(dict)
        }
        this.fosterLesson = getLesson
        this.nowLesson = this.fosterLesson
        this.getYear()
        this.clickYear()
      })
    },

    homeworkChange(file) {
      const fileType = file.name.substring(file.name.lastIndexOf('.') + 1)
      if (fileType !== 'xls' && fileType !== 'xlsx') {
        this.$message.error('请上传.xls或.xlsx格式的文件')
        return false
      }
      const reader = new FileReader()
      reader.onload = () => {
        const data = new Uint8Array(reader.result)
        const workbook = XLSX.read(data, { type: 'array' })
        const sheetNameList = workbook.SheetNames
        const worksheet = workbook.Sheets[sheetNameList[0]]
        const excelData = XLSX.utils.sheet_to_json(worksheet, { header: 1 })
        this.name = excelData[0]
        this.score = excelData[1]
      }
      reader.readAsArrayBuffer(file.raw)
    },

    homeworkClick(row) {
      this.uploadLesson = row.name
      this.uploadYear = row.year
      this.homeworkVisible = true
    },

    homeworkSure() {
      if (this.name == '' && this.score == '') {
        this.$message.error("未上传文件")
      } else {
        let home = ''
        let sum = 0
        for (let i in this.score) {
          sum = sum + this.score[i]
        }
        home = (sum / this.score.length).toString()
        let exp = ''
        let exam = ''
        uploadData(this.uploadLesson, this.uploadYear, home, exp, exam).then(response => {
          console.log(response.data.code)
        })
        this.homeworkVisible = false;
        this.$message.success("上传成功！")
      }
      //接口上传name，score，uploadYear，uploadLesson
      this.name = []
      this.score = []
    },

    homeworkCancel() {
      this.homeworkVisible = false;
      this.name = []
      this.score = []
    },

    examChange(file) {
      const fileType = file.name.substring(file.name.lastIndexOf('.') + 1)
      if (fileType !== 'xls' && fileType !== 'xlsx') {
        this.$message.error('请上传.xls或.xlsx格式的文件')
        return false
      }
      const reader = new FileReader()
      reader.onload = () => {
        const data = new Uint8Array(reader.result)
        const workbook = XLSX.read(data, { type: 'array' })
        const sheetNameList = workbook.SheetNames
        const worksheet = workbook.Sheets[sheetNameList[0]]
        const excelData = XLSX.utils.sheet_to_json(worksheet, { header: 1 })
        this.name = excelData[0]
        this.score = excelData[1]
      }
      reader.readAsArrayBuffer(file.raw)
    },

    examClick(row) {
      this.uploadLesson = row.name
      this.uploadYear = row.year
      this.examVisible = true
    },

    examSure() {
      if (this.name == '' && this.score == '') {
        this.$message.error("未上传文件")
      } else {
        let home = ''
        let exp = ''
        let exam = ''
        let sum = 0
        for (let i in this.score) {
          sum = sum + this.score[i]
        }
        exam = (sum / this.score.length).toString()
        uploadData(this.uploadLesson, this.uploadYear, home, exp, exam).then(response => {
          console.log(response.data.code)
        })
        this.examVisible = false;
        this.$message.success("上传成功！")
      }
      //接口上传name，score，uploadYear，uploadLesson
      this.name = []
      this.score = []
    },

    examCancel() {
      this.examVisible = false;
      this.name = []
      this.score = []
    },

    experimentChange(file) {
      const fileType = file.name.substring(file.name.lastIndexOf('.') + 1)
      if (fileType !== 'xls' && fileType !== 'xlsx') {
        this.$message.error('请上传.xls或.xlsx格式的文件')
        return false
      }
      const reader = new FileReader()
      reader.onload = () => {
        const data = new Uint8Array(reader.result)
        const workbook = XLSX.read(data, { type: 'array' })
        const sheetNameList = workbook.SheetNames
        const worksheet = workbook.Sheets[sheetNameList[0]]
        const excelData = XLSX.utils.sheet_to_json(worksheet, { header: 1 })
        this.name = excelData[0]
        this.score = excelData[1]
      }
      reader.readAsArrayBuffer(file.raw)
    },

    experimentClick(row) {
      this.uploadLesson = row.name
      this.uploadYear = row.year
      this.experimentVisible = true
    },

    experimentSure() {
      //接口上传name，score，uploadYear，uploadLesson
      if (this.name == '' && this.score == '') {
        this.$message.error("未上传文件")
      } else {
        let home = ''
        let exp = ''
        let exam = ''
        let sum = 0
        for (let i in this.score) {
          sum = sum + this.score[i]
        }
        exp = (sum / this.score.length).toString()
        uploadData(this.uploadLesson, this.uploadYear, home, exp, exam).then(response => {
          console.log(response.data.code)
        })
        this.experimentVisible = false;
        this.$message.success("上传成功！")
      }
      //接口上传name，score，uploadYear，uploadLesson
      this.name = []
      this.score = []
    },

    experimentCancel() {
      this.experimentVisible = false;
      this.name = []
      this.score = []
    },

    homeworkExample() {
      let a = document.createElement("a");
      a.href = "./static/example.xlsx"
      a.download = "example.xlsx"
      a.style.display = "none"
      document.body.appendChild(a);
      a.click();
      a.remove();
      this.homeworkVisible = false;
    },

    examExample() {
      let a = document.createElement("a");
      a.href = "./static/example.xlsx"
      a.download = "example.xlsx"
      a.style.display = "none"
      document.body.appendChild(a);
      a.click();
      a.remove();
      this.examVisible = false;
    },

    experimentExample() {
      let a = document.createElement("a");
      a.href = "./static/example.xlsx"
      a.download = "example.xlsx"
      a.style.display = "none"
      document.body.appendChild(a);
      a.click();
      a.remove();
      this.experimentVisible = false;
    }
  },
}
</script>

<style>
.class_data_sideBar {
  width: 100%;
  height: 50px;
  display: flex;
  margin-bottom: 5px;
}

.data_select {
  margin-top: 2px;
  margin-left: 40px;
  font-size: 18px;
  width: 300px;
}

.analyse_side_btn {
  float: left;
  position: relative;
  border-radius: 5px;
  border: 1px solid #93358c;
  background-color: #FFFFFF;
  color: #93358c;
  margin-left: 25px;
  margin-right: 10px;
  margin-top: 5px;
  width: 100px;
}

.analyse_side_btn:hover {
  background-color: #93358c;
  color: #FFFFFF;
}

/*下面是数据分析css*/
.course_completion {
  width: 1300px;
  margin-top: 20px;
  margin-left: 20px;
}

/* 下面为数据上传所用css*/
.dialog_btn {
  float: left;
  margin-left: 100px;
  margin-right: 40px;
}
</style>