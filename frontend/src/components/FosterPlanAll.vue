<template>
  <div class="foster_plan_all" v-if="this.changeNum == 1">

    <div class="plan_all_sideBar">

      <div class="plan_select">
        学院：
        <el-select v-model="selectedFacility" placeholder="所有" size="large">
          <el-option v-for="item in facilitys" :key="item" :value="item" @click="clickFacility()" />
        </el-select>
      </div>

      <div class="plan_select">
        专业：
        <el-select v-model="selectedSubject" placeholder="所有" no-data-text="无" size="large">
          <el-option v-for="item in subjects" :key="item" :value="item" @click="clickSubject()" />
        </el-select>
      </div>

      <div class="plan_select">
        年份：
        <el-select v-model="selectedYear" placeholder="所有" size="large">
          <el-option v-for="item in years" :key="item" :value="item" @click="clickYear()" />
        </el-select>
      </div>

    </div>

    <el-table :data="nowPlan" style="width: 98%; font-size: 18px; margin-left: 15px" max-height="650" size="large"
      empty-text="暂无数据">
      <el-table-column prop="facility" label="学院" />
      <el-table-column prop="subject" label="专业" />
      <el-table-column prop="year" label="年份" />
      <el-table-column fixed="right" label="操作">
        <template #default="scope">
          <el-button link type="success" size="large" @click="downloadFoster(scope.row)">
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
import { getAll } from '../api/api.js'
import jsPDF from "jspdf";
import "jspdf-autotable";

export default {
  name: 'FosterPlanAll',
  components: {
    ElSelect,
    ElButton,
    ElTable,
  },

  data() {
    return {
      changeNum: 1,
      selectedFacility: 'all',
      selectedSubject: 'all',
      selectedYear: 'all',
      facilitys: ["all",],
      subjects: ["all",],
      years: ["all",],
      nowPlan: [],
      fosterPlan: [],
    }
  },

  methods: {

    clickFacility() {
      this.selectedSubject = 'all'
      this.subjects = ['all',]
      this.selectedYear = 'all'
      this.years = ['all',]
      this.nowPlan = []
      if (this.selectedFacility === 'all') {
        for (let item in this.fosterPlan) {
          this.nowPlan.push(this.fosterPlan[item])
        }
      } else {
        for (let item in this.fosterPlan) {
          if (this.fosterPlan[item].facility === this.selectedFacility) {
            this.nowPlan.push(this.fosterPlan[item])
          }
        }
        this.getSubject()
      }
      this.getYear()
    },

    clickSubject() {
      this.selectedYear = 'all'
      this.years = ['all',]
      this.nowPlan = []
      if (this.selectedSubject === 'all') {
        if (this.selectedFacility === 'all') {
          for (let item in this.fosterPlan) {
            this.nowPlan.push(this.fosterPlan[item])
          }
        } else {
          for (let item in this.fosterPlan) {
            if (this.fosterPlan[item].facility === this.selectedFacility) {
              this.nowPlan.push(this.fosterPlan[item])
            }
          }
        }
      } else {
        for (let item in this.fosterPlan) {
          if (this.fosterPlan[item].facility === this.selectedFacility && this.fosterPlan[item].subject === this.selectedSubject) {
            this.nowPlan.push(this.fosterPlan[item])
          }
        }
      }
      this.getYear()
    },

    clickYear() {
      this.nowPlan = []
      if (this.selectedYear === 'all') {
        if (this.selectedFacility === 'all') {
          for (let item in this.fosterPlan) {
            this.nowPlan.push(this.fosterPlan[item])
          }
        } else {
          if (this.selectedSubject === 'all') {
            for (let item in this.fosterPlan) {
              if (this.fosterPlan[item].facility === this.selectedFacility) {
                this.nowPlan.push(this.fosterPlan[item])
              }
            }
          } else {
            for (let item in this.fosterPlan) {
              if (this.fosterPlan[item].facility === this.selectedFacility && this.fosterPlan[item].subject === this.selectedSubject) {
                this.nowPlan.push(this.fosterPlan[item])
              }
            }
          }
        }
      } else {
        if (this.selectedFacility === 'all') {
          for (let item in this.fosterPlan) {
            if (this.fosterPlan[item].year === this.selectedYear) {
              this.nowPlan.push(this.fosterPlan[item])
            }
          }
        } else {
          if (this.selectedSubject === 'all') {
            for (let item in this.fosterPlan) {
              if (this.fosterPlan[item].facility === this.selectedFacility && this.fosterPlan[item].year === this.selectedYear) {
                this.nowPlan.push(this.fosterPlan[item])
              }
            }
          } else {
            for (let item in this.fosterPlan) {
              if (this.fosterPlan[item].facility === this.selectedFacility && this.fosterPlan[item].subject === this.selectedSubject && this.fosterPlan[item].year === this.selectedYear) {
                this.nowPlan.push(this.fosterPlan[item])
              }
            }
          }
        }
      }
    },

    getSubject() {
      this.selectedSubject = 'all'
      this.subjects = ["all",]
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
      let temp = []
      this.years = ["all",]
      this.selectedYear = 'all'
      if (this.selectedFacility === 'all') {
        for (let item in this.fosterPlan) {
          if (temp.indexOf(this.fosterPlan[item].year) === -1) {
            temp.push(this.fosterPlan[item].year)
          }
        }
      } else if (this.selectedFacility !== 'all' && this.selectedSubject === 'all') {
        for (let item in this.fosterPlan) {
          if (this.fosterPlan[item].facility === this.selectedFacility) {
            if (temp.indexOf(this.fosterPlan[item].year) === -1) {
              temp.push(this.fosterPlan[item].year)
            }
          }
        }
      } else if (this.selectedFacility !== 'all' && this.selectedSubject !== 'all') {
        for (let item in this.fosterPlan) {
          if (this.fosterPlan[item].facility === this.selectedFacility && this.fosterPlan[item].subject === this.selectedSubject) {
            if (temp.indexOf(this.fosterPlan[item].year) === -1) {
              temp.push(this.fosterPlan[item].year)
            }
          }
        }
      }
      temp.sort()
      for (let i = 0; i < temp.length; i++) {
        this.years.push(temp[i])
      }
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
        console.log(response.data);
        this.fosterPlan = response.data.content
        this.nowPlan = this.fosterPlan
        this.getFacility()
        this.clickFacility()
      })
    },

    downloadFoster(row) {
      //  存在中文乱码问题！！！！！！！！！！！！！！！！！！！！！！！！！未解决
      console.log(row)
      // let facility = row.facility
      // let subject = row.subject
      // let year = row.year
      const doc = new jsPDF("p", "pt");
      // const headers = ["facility", "subject", "year"];
      // const rows = []
      // rows.push(facility)
      // rows.push(subject)
      // rows.push(year)

      doc.text(270, 60, "FosterPlan")
      // doc.autoTable({
      //   startY: 120,
      //   head: [headers],
      //   body: rows
      // });

      doc.save("FosterPlan.pdf");
    }

  },

  mounted() {
    this.getFosterPlan()
  }

}
</script>

<style>
.plan_all_sideBar {
  width: 100%;
  height: 50px;
  margin-bottom: 5px;
  display: flex;
}

.plan_select {
  font-size: 18px;
  margin-left: 30px;
  width: 300px;
}
</style>

