<template>
  <div class="class_plan_create" v-if="this.changeNum == 1">

    <div class="class_own_sideBar">

      <div class="year_select">
        年份：
        <el-select v-model="selectedYear" placeholder="所有" size="large">
          <el-option v-for="item in years" :key="item" :value="item" @click="clickYear()" />
        </el-select>
      </div>

      <el-button class="btn_lesson_new" type="success" size="large" @click="newClassDialogVisible = true">新建</el-button>

      <el-dialog v-model="newClassDialogVisible" title="新建大纲">
        <el-form ref="form">
          <el-form-item label="课程：">
            <el-input v-model="this.newClassName" @change="updateNewClassName"></el-input>
          </el-form-item>
          <el-form-item label="专业：">
            <el-input v-model="this.newClassSubject" @change="updateNewClassSubject"></el-input>
          </el-form-item>
          <el-form-item label="适用年级：">
            <el-input v-model="this.newClassYear" @change="updateNewClassYear"></el-input>
          </el-form-item>
        </el-form>
        <div>
          <el-button @click="this.clearDataForClassPlan()">取消</el-button>
          <el-button type="primary" @click="newClass();">确认</el-button>
        </div>
      </el-dialog>

    </div>

    <el-table :data="nowOwnLesson" style="width: 95%; font-size: 18px; margin-left: 30px" max-height="650" size="large"
      empty-text="暂无数据">
      <el-table-column prop="name" label="课程" />
      <el-table-column prop="year" label="年份" />
      <el-table-column fixed="right" label="操作">
        <template #default="scope">
          <el-button link type="success" size="large" @click="downloadMyClass(scope.row)">
            下载
          </el-button>
          <el-button link type="danger" size="large" @click="deleteMyClass(scope.row)">
            删除
          </el-button>
        </template>
      </el-table-column>
    </el-table>

  </div>

  <NewDoc v-else-if="this.changeNum == 3" @toClassPlanManage="toClassPlanManage()"
    @clearDataForClassPlan="clearDataForClassPlan()"></NewDoc>
</template>

<script>

import { ElSelect } from 'element-plus'
import { ElTable } from 'element-plus'
import { ElButton } from 'element-plus'
import NewDoc from './classmanage/NewDoc.vue'
import { mapState, mapMutations } from 'vuex';
import { getMine, deleteCP, deleteCContent, deleteCH, deleteCData, deleteCDR, deleteIPC, deleteIPR } from '../api/api.js'
import jsPDF from "jspdf";
import "jspdf-autotable";


export default {
  inject: ['globalData'],
  name: 'ClassPlanCreate',
  components: {
    ElSelect,
    ElButton,
    ElTable,
    NewDoc,
  },

  data() {
    return {
      changeNum: 1,
      selectedYear: 'all',
      years: ["all",],
      nowOwnLesson: [],
      fosterOwnLesson: [],
      newClassName: '',
      newClassSubject: '',
      newClassYear: '',

      //新建课程大纲对话框
      newClassDialogVisible: false
    }
  },

  computed: {
    ...mapState(["newClassNameStore", "newClassSubjectStore", "newClassYearStore"]),
  },

  methods: {

    clickYear() {
      this.nowOwnLesson = []
      if (this.selectedYear === 'all') {
        for (let item in this.fosterOwnLesson) {
          this.nowOwnLesson.push(this.fosterOwnLesson[item])
        }
      } else {
        for (let item in this.fosterOwnLesson) {
          if (this.fosterOwnLesson[item].year === this.selectedYear) {
            this.nowOwnLesson.push(this.fosterOwnLesson[item])
          }
        }
      }
    },

    getYear() {
      let temp = []
      for (let item in this.fosterOwnLesson) {
        if (temp.indexOf(this.fosterOwnLesson[item].year) === -1) {
          temp.push(this.fosterOwnLesson[item].year)
        }
      }
      temp.sort()
      for (let i = 0; i < temp.length; i++) {
        this.years.push(temp[i])
      }
    },

    getfosterOwnLesson() {
      // let getOwnLesson = [
      //   {
      //     name: "数据库原理",
      //     year: "2020",
      //   },
      // ]
      let userAccount = this.globalData.account
      getMine(userAccount).then(response => {
        let getOwnLesson = []
        for (let i in response.data.content) {
          let dict = {}
          dict.name = response.data.content[i].className
          dict.year = response.data.content[i].year
          getOwnLesson.push(dict)
        }
        this.fosterOwnLesson = getOwnLesson
        this.nowOwnLesson = this.fosterOwnLesson
        this.getYear()
        this.clickYear()
      })

    },

    downloadMyClass(row) {
      //  存在中文乱码问题！！！！！！！！！！！！！！！！！！！！！！！！！未解决
      console.log(row)
      // let name = row.name
      // let year = row.year
      const doc = new jsPDF("p", "pt");
      // const headers = ["name", "year"];
      // const rows = []
      // rows.push(name)
      // rows.push(year)

      doc.text(270, 60, "ClassPlan")
      // doc.autoTable({
      //   startY: 120,
      //   head: [headers],
      //   body: rows
      // });

      doc.save("ClassPlan.pdf");
    },

    deleteMyClass(row) {
      let getName = row.name
      let getYear = row.year

      //调用接口删除对应class, deleteCP, deleteCContent, deleteCH, deleteCData, deleteCDR, deleteIPC, deleteIPR
      deleteCP(getName, getYear).then(response => {
        console.log("ClassPlan", response.data.code)
      })
      deleteCContent(getName, getYear).then(response => {
        console.log("ClassContent", response.data.code)
      })
      deleteCH(getName, getYear).then(response => {
        console.log("ClassHours", response.data.code)
      })
      deleteCData(getName, getYear).then(response => {
        console.log("ClassData", response.data.code)
      })
      deleteCDR(getName, getYear).then(response => {
        console.log("ClassDataRatio", response.data.code)
      })
      deleteIPC(getName, getYear).then(response => {
        console.log("IndexPointContent", response.data.code)
      })
      deleteIPR(getYear, getName).then(response => {
        console.log("IndexPointResult", response.data.code)
      })
      this.selectedYear = 'all'
      this.years = ["all",]
      this.nowOwnLesson = []
      this.fosterOwnLesson = []
      this.getfosterOwnLesson()
      this.getYear()
      this.clickYear()
    },


    //新建课程大纲
    newClass() {
      //先确认该课程是否在教学计划中，在教学计划中则跳转编辑，否则提示错误(未实现)
      if (this.newClassName == '' || this.newClassSubject == '' || this.newClassYear == '') {
        this.$message.error("请完善课程信息")
      } else {
        this.changeNum = 3;
      }
    },

    //课程大纲提交或取消后回到大纲管理界面
    toClassPlanManage() {
      this.changeNum = 1
      this.getfosterOwnLesson()
      this.getYear()
      this.clickYear()
    },

    //取消创建大纲时，清空填写的课程名、专业、年份 并 关闭dialog
    clearDataForClassPlan() {
      this.newClassName = ''
      this.newClassSubject = ''
      this.newClassYear = ''
      this.updateNewClassName();
      this.updateNewClassSubject();
      this.updateNewClassYear();
      this.newClassDialogVisible = false;
    },

    ...mapMutations(["updateNewClassNameStore", "updateNewClassSubjectStore", "updateNewClassYearStore"]),

    updateNewClassName() {
      this.updateNewClassNameStore(this.newClassName)
    },

    updateNewClassSubject() {
      this.updateNewClassSubjectStore(this.newClassSubject)
    },

    updateNewClassYear() {
      this.updateNewClassYearStore(this.newClassYear)
    },

  },

  mounted() {
    this.getfosterOwnLesson()
    this.getYear()
    this.clickYear()
  }

}
</script>

<style>
.class_own_sideBar {
  width: 100%;
  height: 50px;
  display: flex;
  margin-bottom: 5px;
}

.year_select {
  margin-top: 2px;
  margin-left: 45px;
  font-size: 18px;
  width: 300px;
}

.btn_lesson_new {
  margin-top: 2px;
  margin-left: 10px;
}
</style>

