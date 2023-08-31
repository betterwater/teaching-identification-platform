<template>
  <div class="foster_plan_create">
    <el-container class="plan_create_layout">

      <el-container class="plan_create_container">

        <el-aside class="aside_plan_directory" width="210px">
          <el-menu default-active="1">
            <el-menu-item index="1" class="plan_directory_item" @click="switchPlanItem(1)">
              <div class="btn_bgcolor"></div>培养方案创建>
            </el-menu-item>
            <el-menu-item index="2" class="plan_directory_item" @click="switchPlanItem(2)">
              <div class="btn_bgcolor"></div>专业培养目标及要求
            </el-menu-item>
            <el-menu-item index="3" class="plan_directory_item" @click="switchPlanItem(3)">
              <div class="btn_bgcolor"></div>毕业要求及指标点
            </el-menu-item>
            <el-menu-item index="4" class="plan_directory_item" @click="switchPlanItem(4)">
              <div class="btn_bgcolor"></div>培养目标与毕业要求对应表
            </el-menu-item>
            <el-menu-item index="5" class="plan_directory_item" @click="switchPlanItem(5)">
              <div class="btn_bgcolor"></div>教学计划表
            </el-menu-item>
            <el-menu-item index="6" class="plan_directory_item" @click="switchPlanItem(6)">
              <div class="btn_bgcolor"></div>课程权重
            </el-menu-item>
            <el-menu-item index="7" class="plan_directory_item" @click="switchPlanItem(7)">
              <div class="btn_bgcolor"></div>课程对毕业要求支撑关系
            </el-menu-item>
            <el-menu-item index="8" class="plan_directory_item" @click="switchPlanItem(8)">
              <div class="btn_bgcolor"></div>评价机制
            </el-menu-item>
          </el-menu>
        </el-aside>

        <el-main>

          <!-- 培养方案创建 -->
          <div class="foster_plan_info" v-if="this.showPlanItemIndex == '1'">
            <CreateFosterPlan></CreateFosterPlan>
          </div>

          <!-- 专业培养目标及要求 -->
          <div class="foster_plan_info" v-if="this.showPlanItemIndex == '2'">
            <CultivationGoal></CultivationGoal>
          </div>

          <!-- 毕业要求及指标点 -->
          <div class="foster_plan_info" v-if="this.showPlanItemIndex == '3'">
            <GraduateRequest></GraduateRequest>
          </div>

          <!-- 培养目标与毕业要求对应表 -->
          <div class="foster_plan_info" v-if="this.showPlanItemIndex == '4'">
            <GoalAndRequest></GoalAndRequest>
          </div>

          <!-- 教学计划表 -->
          <div class="foster_plan_info" v-if="this.showPlanItemIndex == '5'">
            <CourseInFosterPlan></CourseInFosterPlan>
          </div>

          <!-- 课程权重 -->
          <div class="foster_plan_info" v-if="this.showPlanItemIndex == '6'">
            <CourseWeight></CourseWeight>
          </div>

          <!-- 课程对毕业要求支撑关系 -->
          <div class="foster_plan_info" v-if="this.showPlanItemIndex == '7'">
            <CourseAndRequest></CourseAndRequest>
          </div>

          <!-- 评价机制 -->
          <div class="foster_plan_info" v-if="this.showPlanItemIndex == '8'">
            <EvaluationMechanism></EvaluationMechanism>
          </div>

        </el-main>

      </el-container>
      <el-footer>
        <div class="submit_region">
          <button class="btn_submit" @click="saveFosterPlan()">提交</button>
          <button class="btn_submit_not" @click="cleanDataInFosterPlan(); backToFosterPlanAll()">取消</button>
        </div>
      </el-footer>
    </el-container>
  </div>
</template>

<script>

import { ElContainer, ElAside, ElMain, ElFooter } from 'element-plus';
import { mapMutations, mapState } from 'vuex';
import CreateFosterPlan from './fosterplancreate/CreateFosterPlan.vue'
import CultivationGoal from './fosterplancreate/CultivationGoal.vue';
import GraduateRequest from './fosterplancreate/GraduateRequest.vue'
import GoalAndRequest from './fosterplancreate/GoalAndRequest.vue'
import CourseInFosterPlan from './fosterplancreate/CourseInFosterPlan.vue';
import CourseWeight from './fosterplancreate/CourseWeight.vue';
import CourseAndRequest from './fosterplancreate/CourseAndRequest.vue';
import EvaluationMechanism from './fosterplancreate/EvaluationMechanism.vue';
import { uploadPlan, uploadCG, uploadRequest, uploadGR, uploadCIFP, uploadCW, uploadCSR } from '../api/api.js'

export default {
  name: 'FosterPlanCreate',
  components: {
    ElContainer,
    ElAside,
    ElMain,
    ElFooter,
    CreateFosterPlan,
    CultivationGoal,
    GraduateRequest,
    GoalAndRequest,
    CourseInFosterPlan,
    CourseWeight,
    CourseAndRequest,
    EvaluationMechanism
  },

  data() {
    return {
      showPlanItemIndex: '1',
      confirm: false
    }
  },

  computed: {
    ...mapState(["facilityStore", "subjectStore", "yearStore",
      "briefInfoStore", "subjectDescriptionStore", "tableDataCultivationGoal",
      "graduateRequestTable", "GoalMatchRequest", "tableCourseInFosterplan",
      "CourseMatchRequest", "CourseSupportRequest", "evaluationMechanismStore"]),
  },

  methods: {
    ...mapMutations(["cleanFosterPlan"]),

    switchPlanItem(num) {
      this.showPlanItemIndex = num;
    },

    //培养方案创建完成后的保存
    saveFosterPlan() {
      if (this.facilityStore == '' || this.subjectStore == '' || this.yearStore == '') this.$message.error("请将学院、专业、年级填写完整")
      else {
        //上传培养方案基本信息
        uploadPlan(
          this.facilityStore,
          this.yearStore,
          this.subjectStore,
          this.briefInfoStore,
          this.subjectDescriptionStore,
          this.evaluationMechanismStore
        ).then(response => {
          console.log(response.data)
          if (response.data.code == 'lack') {
            this.$message.error("请确保内容填写完整");
          }
          else if (response.data.code == 'exist') {
            this.$message.error("该年级培养方案已存在");
          }
          else {
            this.confirm = true

            // 上传培养目标
            for (let key in this.tableDataCultivationGoal) {
              uploadCG(this.facilityStore,
                this.yearStore,
                this.subjectStore,
                Number(key + 1),
                this.tableDataCultivationGoal[key].CultivationGoal,
                this.tableDataCultivationGoal[key].description).then(response => {
                  console.log(response.data)
                })
            }

            //上传毕业要求
            var requestIndex = 1
            var pointIndex = 1
            for (let key in this.graduateRequestTable) {
              for (let kkey in this.graduateRequestTable[key].points) {
                uploadRequest(this.facilityStore,
                  this.yearStore,
                  this.subjectStore,
                  requestIndex,
                  this.graduateRequestTable[key].info,
                  requestIndex + '-' + pointIndex,
                  this.graduateRequestTable[key].points[kkey].point).then(response => {
                    console.log(response.data)
                  })
                pointIndex += 1
              }
              requestIndex += 1
              pointIndex = 1
            }

            //上传培养目标与毕业要求对应表
            var goalIndex = 0//培养目标序号
            requestIndex = 1
            for (let key in this.GoalMatchRequest) {
              for (let kkey in this.GoalMatchRequest[key]) {
                if (this.GoalMatchRequest[key][kkey] == 1) {
                  goalIndex = Number(kkey.slice(4))
                  uploadGR(this.facilityStore, this.yearStore, this.subjectStore, goalIndex, requestIndex).then(response => {
                    console.log(response.data);
                  })
                }
              }
              requestIndex += 1
            }

            //上传教学计划表
            for (let key in this.tableCourseInFosterplan) {
              uploadCIFP(this.facilityStore,
                this.yearStore,
                this.subjectStore,
                this.tableCourseInFosterplan[key].courseName,
                this.tableCourseInFosterplan[key].courseCategory,
                this.tableCourseInFosterplan[key].credits,
                this.tableCourseInFosterplan[key].hours,
                this.tableCourseInFosterplan[key].semester,
                this.tableCourseInFosterplan[key].isRequired,).then(response => {
                  console.log(response.data);
                })
            }

            //上传课程权重
            for (let key in this.CourseMatchRequest) {
              for (let kkey in this.CourseMatchRequest[key]) {
                if (this.CourseMatchRequest[key][kkey] != 0 && kkey != 'courseName') {
                  uploadCW(this.facilityStore,
                    this.yearStore,
                    this.subjectStore,
                    kkey,
                    this.CourseMatchRequest[key].courseName,
                    this.CourseMatchRequest[key][kkey]).then(response => {
                      console.log(response.data);
                    })
                }
              }
            }

            //课程对毕业要求支撑关系
            for (let key in this.CourseSupportRequest) {
              for (let kkey in this.CourseSupportRequest[key]) {
                if (this.CourseSupportRequest[key][kkey] != '' && kkey != 'courseName') {
                  uploadCSR(this.facilityStore,
                    this.yearStore,
                    this.subjectStore,
                    this.CourseSupportRequest[key].courseName,
                    kkey,
                    this.CourseSupportRequest[key][kkey]).then(response => {
                      console.log(response.data);
                    })
                }
              }
            }

            this.$message({
              message: "提交成功",
              type: "success",
            });
          }

          if (this.confirm) {
            this.confirm = false
            this.cleanDataInFosterPlan();
            this.backToFosterPlanAll();
          }
        })
      }


    },

    //提交完成或取消提交后清除填写的数据项
    cleanDataInFosterPlan() {
      this.cleanFosterPlan();
      console.log("已清除数据项");
    },

    //培养方案提交或取消提交时，返回方案总览界面
    backToFosterPlanAll() {
      this.$emit('toFosterPlanAll');
    }
  }
}

</script>

<style>
.foster_plan_create {
  height: 100%;
  width: 100%;
}

.plan_create_layout {
  height: 100%;
  width: 100%;
}

.plan_create_container {
  width: 100%;
}

.plan_directory_item {
  box-shadow: 0 0 1px #93358c inset;
  border-radius: 3px;
  font-weight: 700;
  color: black !important;
  width: 100%;
  margin-bottom: 10px;
  height: 40px !important;
  padding-left: 0px !important;
}

.plan_directory_item.is-active .btn_bgcolor {
  background-color: #93358c;
}

.btn_bgcolor {
  height: 40px;
  width: 10px;
  border-radius: 3px 0px 0px 3px;
  margin-right: 10px;
  background-color: #d2b5d0;
}

.foster_plan_info {
  width: 96%;
  height: 96%;
  padding-left: 20px;
  padding-top: 20px;
  border-left: 1px solid #93358c;
}

.foster_plan_name {
  width: 220px !important;
  margin-right: 20px;
  margin-top: 10px;
}

.brief_info {
  margin-top: 20px;
  width: 700px !important;
}

/* 培养目标添加按钮 */
.add_cultivation_require_item_btn {
  margin-top: 10px;
  width: 910px;
  border-radius: 3px;
  border: 1px solid #93358c;
  background-color: #FFFFFF;
  color: #93358c;
}

.add_cultivation_require_item_btn:hover {
  background-color: #93358c;
  color: #FFFFFF;
}

.goal_btn {
  border-radius: 3px;
  border: 1px solid #93358c;
  background-color: #FFFFFF;
  color: #93358c;
}

.goal_btn:hover {
  background-color: #93358c;
  color: #FFFFFF;
}

.add_course_in_plan {
  width: 900px;
  padding-top: 15px;
  text-align: center;
}

.dynamic-table {
  width: 700px;
}

.ftplan_item_title {
  font-size: 16px;
  font-weight: 500;
}

.foster_plan_create .el-footer {
  height: 60px;
  border-top: 1px solid #93358c;
}

.submit_region {
  padding-top: 15px;
  text-align: center;
}

.btn_submit {
  padding: 5px 20px;
  margin-right: 50px;
  border-radius: 5px;
  border: 1px solid #93358c;
  background-color: #FFFFFF;
  color: #93358c;
}

.btn_submit_not {
  padding: 5px 20px;
  border-radius: 5px;
  border: 1px solid #93358c;
  background-color: #FFFFFF;
  color: #93358c;
}

.btn_submit:hover,
.btn_submit_not:hover {
  background-color: #93358c;
  color: #FFFFFF;
}
</style>