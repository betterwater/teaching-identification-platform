<template>
  <div class="class_plan_all" v-if="this.changeNum == 1">

    <div class="class_all_sideBar">

      <div class="lesson_select">
        教师：
        <el-select v-model="selectedTeacher" placeholder="所有" size="large">
          <el-option v-for="item in teachers" :key="item" :value="item" @click="clickTeacher()" />
        </el-select>
      </div>

      <div class="lesson_select">
        年份：
        <el-select v-model="selectedYear" placeholder="所有" size="large">
          <el-option v-for="item in years" :key="item" :value="item" @click="clickYear()" />
        </el-select>
      </div>

    </div>

    <el-table :data="nowLesson" style="width: 95%; font-size: 18px; margin-left: 30px" max-height="650" size="large"
      empty-text="暂无数据">
      <el-table-column prop="name" label="课程" />
      <el-table-column prop="teacher" label="教师" />
      <el-table-column prop="year" label="年份" />
      <el-table-column fixed="right" label="操作">
        <template #default="scope">
          <el-button link type="success" size="large" @click="downloadClass(scope.row)">
            下载
          </el-button>
        </template>
      </el-table-column>
    </el-table>

  </div>
</template>

<script>

import { ElSelect } from 'element-plus'
import { ElTable } from 'element-plus'
import { ElButton } from 'element-plus'
import { getAllPlan } from '../api/api.js'
import jsPDF from "jspdf";
import "jspdf-autotable";

export default {
  name: 'ClassPlanAll',
  components: {
    ElSelect,
    ElButton,
    ElTable,
  },

  data() {
    return {
      changeNum: 1,
      selectedTeacher: 'all',
      selectedYear: 'all',
      teachers: ["all",],
      years: ["all",],
      nowLesson: [],
      fosterLesson: []
    }
  },

  methods: {

    clickTeacher() {
      this.nowLesson = []
      if (this.selectedYear === 'all') {
        if (this.selectedTeacher === 'all') {
          for (let item in this.fosterLesson) {
            this.nowLesson.push(this.fosterLesson[item])
          }
        } else {
          for (let item in this.fosterLesson) {
            if (this.fosterLesson[item].teacher === this.selectedTeacher) {
              this.nowLesson.push(this.fosterLesson[item])
            }
          }
        }
      } else {
        if (this.selectedTeacher === 'all') {
          for (let item in this.fosterLesson) {
            if (this.fosterLesson[item].year === this.selectedYear) {
              this.nowLesson.push(this.fosterLesson[item])
            }
          }
        } else {
          for (let item in this.fosterLesson) {
            if (this.fosterLesson[item].teacher === this.selectedTeacher && this.fosterLesson[item].year === this.selectedYear) {
              this.nowLesson.push(this.fosterLesson[item])
            }
          }
        }
      }
      this.getTeacher()
      this.getYear()
    },

    clickYear() {
      this.nowLesson = []
      if (this.selectedTeacher === 'all') {
        if (this.selectedYear === 'all') {
          for (let item in this.fosterLesson) {
            this.nowLesson.push(this.fosterLesson[item])
          }
        } else {
          for (let item in this.fosterLesson) {
            if (this.fosterLesson[item].year === this.selectedYear) {
              this.nowLesson.push(this.fosterLesson[item])
            }
          }
        }
      } else {
        if (this.selectedYear === 'all') {
          for (let item in this.fosterLesson) {
            if (this.fosterLesson[item].teacher === this.selectedTeacher) {
              this.nowLesson.push(this.fosterLesson[item])
            }
          }
        } else {
          for (let item in this.fosterLesson) {
            if (this.fosterLesson[item].teacher === this.selectedTeacher && this.fosterLesson[item].year === this.selectedYear) {
              this.nowLesson.push(this.fosterLesson[item])
            }
          }
        }
      }
      this.getTeacher()
      this.getYear()
    },

    getTeacher() {
      this.teachers = ["all",]
      if (this.selectedYear === 'all') {
        if (this.selectedTeacher === 'all') {
          for (let item in this.fosterLesson) {
            if (this.teachers.indexOf(this.fosterLesson[item].teacher) === -1) {
              this.teachers.push(this.fosterLesson[item].teacher)
            }
          }
        } else {
          for (let item in this.fosterLesson) {
            if (this.fosterLesson[item].teacher === this.selectedTeacher) {
              if (this.teachers.indexOf(this.fosterLesson[item].teacher) === -1) {
                this.teachers.push(this.fosterLesson[item].teacher)
              }
            }
          }
        }
      } else {
        if (this.selectedTeacher === 'all') {
          for (let item in this.fosterLesson) {
            if (this.fosterLesson[item].year === this.selectedYear) {
              if (this.teachers.indexOf(this.fosterLesson[item].teacher) === -1) {
                this.teachers.push(this.fosterLesson[item].teacher)
              }
            }
          }
        }
      }
      this.teachers.sort()
    },

    getYear() {
      let temp = []
      this.years = ["all",]
      if (this.selectedTeacher === 'all') {
        if (this.selectedYear === 'all') {
          for (let item in this.fosterLesson) {
            if (temp.indexOf(this.fosterLesson[item].year) === -1) {
              temp.push(this.fosterLesson[item].year)
            }
          }
        } else {
          for (let item in this.fosterLesson) {
            if (this.fosterLesson[item].year === this.selectedYear) {
              if (temp.indexOf(this.fosterLesson[item].year) === -1) {
                temp.push(this.fosterLesson[item].year)
              }
            }
          }
        }
      } else {
        if (this.selectedYear === 'all') {
          for (let item in this.fosterLesson) {
            if (this.fosterLesson[item].teacher === this.selectedTeacher) {
              if (temp.indexOf(this.fosterLesson[item].year) === -1) {
                temp.push(this.fosterLesson[item].year)
              }
            }
          }
        }
      }
      temp.sort()
      for (let i = 0; i < temp.length; i++) {
        this.years.push(temp[i])
      }
    },

    getFosterLesson() {
      //从数据库获取所有方案的ID、facility、subject、year
      let getLesson = [
        // {
        //   name: "",
        //   teacher: "",
        //   year: "",
        // },
      ]

      getAllPlan().then(response => {
        getLesson.length = 0
        for (var i = 0; i < response.data.content.length; i++) {
          var data = response.data.content[i]
          getLesson.push({
            name: data.className,
            teacher: response.data.userName[i],
            year: data.year,
          })
        }
        this.fosterLesson = getLesson
        this.nowLesson = this.fosterLesson
        this.clickTeacher()
      })
    },

    downloadClass(row) {
      //  存在中文乱码问题！！！！！！！！！！！！！！！！！！！！！！！！！未解决
      console.log(row)
      // let name = row.name
      // let teacher = row.teacher
      // let year = row.year
      const doc = new jsPDF("p", "pt");
      // const headers = ["name", "teacher", "year"];
      // const rows = []
      // rows.push(name)
      // rows.push(teacher)
      // rows.push(year)

      doc.text(270, 60, "ClassPlan")

      // doc.autoTable({
      //   startY: 120,
      //   head: [headers],
      //   body: rows
      // });

      doc.save("ClassPlan.pdf");
    }
  },

  mounted() {
    this.getFosterLesson()
  }

}
</script>

<style>
.class_all_sideBar {
  width: 100%;
  height: 50px;
  display: flex;
  margin-bottom: 5px;
}

.lesson_select {
  margin-top: 2px;
  margin-left: 45px;
  font-size: 18px;
  width: 300px;
}
</style>

