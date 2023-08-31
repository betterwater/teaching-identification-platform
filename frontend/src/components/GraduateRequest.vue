<template>
  <div class="graduate_request">

    <div class="table_all_sideBar">

      <div class="table_select">
        学院：
        <el-select v-model="selectedFacility" placeholder="所有" size="large" no-data-text="暂无数据">
          <el-option v-for="item in facilitys" :key="item" :value="item" @click="clickFacility()" />
        </el-select>
      </div>

      <div class="table_select">
        专业：
        <el-select v-model="selectedSubject" placeholder="所有" no-data-text="无" size="large">
          <el-option v-for="item in subjects" :key="item" :value="item" @click="clickSubject()" />
        </el-select>
      </div>

      <div class="table_select">
        年份：
        <el-select v-model="selectedYear" placeholder="所有" no-data-text="无" size="large">
          <el-option v-for="item in years" :key="item" :value="item" @click="clickYear()" />
        </el-select>
      </div>

    </div>

    <el-button style="margin-left: 30px;" @click="calculateGraduateCompletion">计算完成度</el-button>
    <el-table :data="tableData" :span-method="objectSpanMethod" border size="mini" class="table_for_graduate"
      max-height="600px" empty-text="暂无数据">
      <el-table-column prop="graduateRequests" label="毕业要求" align="center" width="100px"> </el-table-column>
      <el-table-column prop="graduateRequestScores" label="毕业要求达成值" align="center" width="130px"> </el-table-column>
      <el-table-column prop="graduationPoints" label="毕业要求指标点" align="center" width="130px"> </el-table-column>
      <el-table-column prop="graduationPointScores" label="指标点达成值" align="center" width="110px"> </el-table-column>
      <el-table-column prop="courses" label="支撑课程" align="center" width="180px"> </el-table-column>
      <el-table-column prop="courseWeights" label="课程达成度目标值" align="center" width="140px"> </el-table-column>
      <el-table-column prop="courseScores" label="课程达成度实际值" align="center" width="180px"> </el-table-column>
    </el-table>
  </div>
</template>

<script>
import { ElSelect } from 'element-plus'
import { getPointW, getPoint, getAll } from '../api/api.js'

export default {
  name: 'GraduateRequest',
  components: {
    ElSelect,
  },

  data() {
    return {
      selectedFacility: '请选择学院',
      selectedSubject: '',
      selectedYear: '',
      facilitys: [],
      subjects: [],
      years: [],
      fosterPlan: [],

      //上面为筛选所用数据
      dynamicValidateForm: {
        domains: []
      },
      spanArr: [], // 一个空的数组，用于存放每一行记录的合并数
      pos: 0, // spanArr 的索引
      contentSpanArr: [],
      position: 0,

      tableData: [
        // {
        //   graduateRequests:'',//毕业要求
        //   graduateRequestScores:'',//毕业要求实际达成值(下属指标点实际达成值中的最小值)
        //   graduationPoints: '',//毕业要求指标点
        //   graduationPointScores:'',//毕业要求指标点实际达成值
        //   courses:'',//支撑课程
        //   courseWeights: '',//课程达成度目标值(课程占据指标点权重)
        //   courseScores: '',//课程达成度实际值
        // },
      ],
    }
  },

  mounted() {
    this.getFosterPlan();
  },

  methods: {
    // eslint-disable-next-line
    objectSpanMethod({ row, column, rowIndex, columnIndex }) {
      if (columnIndex === 0 || columnIndex === 1) {
        const _row = this.spanArr[rowIndex];
        const _col = _row > 0 ? 1 : 0;
        return {
          rowspan: _row,
          colspan: _col
        };
      } else if (columnIndex === 2 || columnIndex === 3) {
        const _row = this.contentSpanArr[rowIndex];
        const _col = _row > 0 ? 1 : 0;
        return {
          rowspan: _row,
          colspan: _col
        };
      }
    },
    // 获取列表数据
    getList() {
      this.dynamicValidateForm.domains = this.tableData || [];
      // 设定一个数组spanArr/contentSpanArr来存放要合并的格数，同时还要设定一个变量pos/position来记录
      this.spanArr = [];
      this.contentSpanArr = [];
      for (var i = 0; i < this.tableData.length; i++) {
        if (i === 0) {
          this.spanArr.push(1);
          this.pos = 0;
          this.contentSpanArr.push(1);
          this.position = 0;
        } else {
          // 判断当前元素与上一个元素是否相同(第1和第2列)
          if (this.tableData[i].graduateRequests === this.tableData[i - 1].graduateRequests) {
            this.spanArr[this.pos] += 1;
            this.spanArr.push(0);
          } else {
            this.spanArr.push(1);
            this.pos = i;
          }
          // 判断当前元素与上一个元素是否相同(第3列)
          if (this.tableData[i].graduationPoints === this.tableData[i - 1].graduationPoints) {
            this.contentSpanArr[this.position] += 1;
            this.contentSpanArr.push(0);
          } else {
            this.contentSpanArr.push(1);
            this.position = i;
          }
        }
      }
    },

    //下面为筛选框所用函数
    clickFacility() {
      this.subjects = []
      this.years = []
      if (this.selectedFacility === '请选择学院') {
        this.selectedSubject = '请选择学院'
        this.selectedYear = '请选择学院'
      } else {
        this.selectedYear = '请选择专业'
        this.selectedSubject = '请选择专业'
        this.getSubject()
      }
    },

    clickSubject() {
      this.years = []
      if (this.selectedSubject === '请选择专业') {
        this.selectedYear = '请选择专业'
      } else {
        this.selectedYear = '请选择年份'
        this.getYear()
      }
    },

    clickYear() {
      this.getDataForGraduateRequest(this.selectedFacility, this.selectedSubject, this.selectedYear)
    },

    getSubject() {
      for (let item in this.fosterPlan) {
        if (this.fosterPlan[item].facility === this.selectedFacility) {
          if (this.subjects.indexOf(this.fosterPlan[item].subject) === -1) {
            this.subjects.push(this.fosterPlan[item].subject)
          }
        }
      }
      this.subjects.sort()
    },

    getFacility() {
      for (let item in this.fosterPlan) {
        if (this.facilitys.indexOf(this.fosterPlan[item].facility) === -1) {
          this.facilitys.push(this.fosterPlan[item].facility)
        }
      }
      this.facilitys.sort()
    },

    getYear() {
      for (let item in this.fosterPlan) {
        if (this.fosterPlan[item].facility === this.selectedFacility && this.fosterPlan[item].subject === this.selectedSubject) {
          if (this.years.indexOf(this.fosterPlan[item].year) === -1) {
            this.years.push(this.fosterPlan[item].year)
          }
        }
      }
      this.years.sort()
    },

    getFosterPlan() {
      //从数据库获取所有方案的ID、facility、subject、year
      // let getPlan = [
      //   {
      //     facility: "软件学院",
      //     subject: "软件工程",
      //     year: "2020",
      //   },
      // ]
      getAll().then(response => {
        console.log("获取所有培养方案");
        console.log(response.data);
        this.fosterPlan = response.data.content
        this.getFacility()
        this.clickFacility()
      })
    },

    //获取表格所需数据
    getDataForGraduateRequest(selectedFacility, selectedSubject, selectedYear) {
      getPointW(selectedFacility, selectedYear, selectedSubject).then(response => {
        this.tableData.length = 0;
        for (var i = 0; i < response.data.content.length; i++) {
          var data = response.data.content[i];
          this.tableData.push({
            graduateRequests: '毕业要求' + data.pointIndex.slice(0, 1),
            graduateRequestScores: 0,
            graduationPoints: '指标点' + data.pointIndex,
            graduationPointScores: 0,
            courses: data.className,
            courseWeights: data.weight,
            courseScores: 0,
          })
        }

        //对毕业要求表中数据进行排序
        for (var j = 0; j < this.tableData.length; j++) {
          for (i = 0; i < this.tableData.length - 1; i++) {
            let item1 = this.tableData[i]
            let item2 = this.tableData[i + 1]
            let count1 = Number(item1.graduationPoints.charAt(3)) * 10 + Number(item1.graduationPoints.charAt(5))
            let count2 = Number(item2.graduationPoints.charAt(3)) * 10 + Number(item2.graduationPoints.charAt(5))
            if (count1 > count2) {
              this.tableData[i] = this.tableData.splice(i + 1, 1, this.tableData[i])[0]
            }
          }
        }

        //获取课程达成度实际值
        for (let key in this.tableData) {
          //默认毕业要求及单个毕业要求对应指标点均不超过9个
          getPoint(selectedYear, this.tableData[key].courses, this.tableData[key].graduationPoints.slice(3)).then(response => {
            console.log(response.data);
            if (response.data.code == 'false') {
              this.tableData[key].courseScores = '该课程尚未计算完成度'
            } else {
              this.tableData[key].courseScores = Number(response.data.content[0].goal)
            }
          })
        }

        this.getList();
      })
    },

    calculateGraduateCompletion() {
      //计算指标点达成值
      var completion = {};
      for (let key in this.tableData) {
        if (!(this.tableData[key].graduationPoints in completion)) {
          completion[this.tableData[key].graduationPoints] = 0
        }
        if (this.tableData[key].courseScores != '该课程尚未计算完成度') {
          completion[this.tableData[key].graduationPoints] += this.tableData[key].courseScores
        }
      }
      for (let key in this.tableData) {
        this.tableData[key].graduationPointScores = completion[this.tableData[key].graduationPoints]
      }

      //计算毕业要求达成值
      var graduateCompletion = {};
      for (let key in this.tableData) {
        if (!(this.tableData[key].graduateRequests in graduateCompletion)) {
          graduateCompletion[this.tableData[key].graduateRequests] = 1
        }
        if (this.tableData[key].graduationPointScores < graduateCompletion[this.tableData[key].graduateRequests])
          graduateCompletion[this.tableData[key].graduateRequests] = this.tableData[key].graduationPointScores
      }
      for (let key in this.tableData) {
        this.tableData[key].graduateRequestScores = graduateCompletion[this.tableData[key].graduateRequests]
      }
    }
  }
}
</script>

<style>
.table_for_graduate {
  width: fit-content;
  margin-left: 30px;
  margin-top: 20px;
}

.table_all_sideBar {
  width: 100%;
  height: 50px;
  margin-bottom: 20px;
  display: flex;
}

.table_select {
  font-size: 18px;
  margin-left: 30px;
  width: 300px;
}
</style>