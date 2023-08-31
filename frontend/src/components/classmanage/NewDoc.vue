<template>
  <div class="new_doc">
    <el-container class="plan_create_layout">

      <el-container class="plan_create_container">

        <el-aside class="aside_plan_directory" width="210px">
          <el-menu default-active="1">
            <el-menu-item index="1" class="plan_directory_item" @click="switchOutlineItem(1)">
              <div class="btn_bgcolor"></div>大纲创建>
            </el-menu-item>
            <el-menu-item index="2" class="plan_directory_item" @click="switchOutlineItem(2)">
              <div class="btn_bgcolor"></div>课程内容
            </el-menu-item>
            <el-menu-item index="3" class="plan_directory_item" @click="switchOutlineItem(3)">
              <div class="btn_bgcolor"></div>学时分配
            </el-menu-item>
            <el-menu-item index="4" class="plan_directory_item" @click="switchOutlineItem(4)">
              <div class="btn_bgcolor"></div>课程目标
            </el-menu-item>
            <el-menu-item index="5" class="plan_directory_item" @click="switchOutlineItem(5)">
              <div class="btn_bgcolor"></div>评价方式
            </el-menu-item>
          </el-menu>
        </el-aside>

        <el-main>

          <!-- 大纲创建> -->
          <div class="foster_plan_info" v-if="this.showOutlineItemIndex == '1'">
            <CreateCourseOutline></CreateCourseOutline>
          </div>

          <!-- 课程内容 -->
          <div class="foster_plan_info" v-if="this.showOutlineItemIndex == '2'">
            <CourseContent></CourseContent>
          </div>

          <!-- 学时分配 -->
          <div class="foster_plan_info" v-if="this.showOutlineItemIndex == '3'">
            <HoursAllocation></HoursAllocation>
          </div>

          <!-- 课程目标 -->
          <div class="foster_plan_info" v-if="this.showOutlineItemIndex == '4'">
            <CourseGoal></CourseGoal>
          </div>

          <!-- 评价方式 -->
          <div class="foster_plan_info" v-if="this.showOutlineItemIndex == '5'">
            <AssessmentMethod></AssessmentMethod>
          </div>

        </el-main>

      </el-container>
      <el-footer>
        <div class="submit_region">
          <button class="btn_submit"
            @click="saveClassPlan(); this.clearClassPlan(); this.backToClassPlanManage()">提交</button>
          <button class="btn_submit_not" @click="this.clearClassPlan(); this.backToClassPlanManage()">取消</button>
        </div>
      </el-footer>
    </el-container>
  </div>
</template>
  
<script>
import { ElContainer, ElAside, ElMain, ElFooter } from 'element-plus'
import CreateCourseOutline from '../newdoc/CreateCourseOutline.vue'
import CourseContent from '../newdoc/CourseContent.vue'
import CourseGoal from '../newdoc/CourseGoal.vue'
import HoursAllocation from '../newdoc/HoursAllocation.vue'
import AssessmentMethod from '../newdoc/AssessmentMethod.vue'
import { mapState, mapMutations } from 'vuex';
import { uploadClass, uploadIPC, uploadRatio, uploadCC, uploadCH } from '../../api/api.js'


export default {
  inject: ['globalData'],
  name: 'NewDoc',
  components: {
    ElContainer,
    ElAside,
    ElMain,
    ElFooter,
    CreateCourseOutline,
    CourseContent,
    CourseGoal,
    HoursAllocation,
    AssessmentMethod
  },

  data() {
    return {
      //大纲创建不同部分切换
      showOutlineItemIndex: '1',
    }
  },

  computed: {
    ...mapState(["newClassNameStore", "newClassSubjectStore", "newClassYearStore",
      "courseBriefInfoStore", "courseGoalWeightTable", "chapterData", "courseGoalTable"]),
  },

  methods: {
    ...mapMutations(["clearClassPlan"]),

    switchOutlineItem(num) {
      this.showOutlineItemIndex = num;
    },

    saveClassPlan() {
      //上传新建大纲基本信息：用户账号、课程名、年份、课程简介
      uploadClass(this.globalData.account, this.newClassNameStore, this.newClassYearStore, this.courseBriefInfoStore).then(response => {
        console.log("上传新建大纲基本信息：用户账号、课程名、年份、课程简介");
        console.log(response.data)
      })

      //上传课程目标对于指标点权重
      for (let key in this.courseGoalWeightTable) {
        uploadIPC(
          this.newClassNameStore,
          this.newClassYearStore,
          this.courseGoalWeightTable[key].courseGoalIndex,
          this.courseGoalWeightTable[key].courseGoal,
          this.courseGoalWeightTable[key].pointIndex,
          this.courseGoalWeightTable[key].weight
        ).then(response => {
          console.log("上传课程目标对于指标点权重");
          console.log(response.data)
        })
      }

      //上传课程目标考核方式权重
      for (let key in this.courseGoalTable) {
        uploadRatio(
          this.newClassNameStore,
          this.newClassYearStore,
          Number(key) + 1,
          this.courseGoalTable[key].homeworkRatio,
          this.courseGoalTable[key].examRatio,
          this.courseGoalTable[key].experienceRatio
        ).then(response => {
          console.log("上传课程目标考核方式权重");
          console.log(response.data)
        })
      }

      //上传课程内容
      var chapterIndex = 1
      var keyPointIndex = 1
      for (let key in this.chapterData) {
        for (let kkey in this.chapterData[key].keyPoints) {
          uploadCC(
            this.newClassNameStore,
            this.newClassYearStore,
            chapterIndex,
            this.chapterData[key].chapterName,
            keyPointIndex,
            this.chapterData[key].keyPoints[kkey].keyPoint
          ).then(response => {
            console.log("上传课程内容");
            console.log(response.data)
          })
          keyPointIndex += 1
        }
        chapterIndex += 1
        keyPointIndex = 1
      }

      //上传学时分配信息
      chapterIndex = 1
      for (let key in this.chapterData) {
        uploadCH(
          this.newClassNameStore,
          this.newClassYearStore,
          chapterIndex,
          this.chapterData[key].theoryHours,
          this.chapterData[key].practiceHours,
          this.chapterData[key].selfLearningHours,
          this.chapterData[key].description
        ).then(response => {
          console.log("上传学时分配信息");
          console.log(response.data);
        })
      }

      this.$message.success("提交成功")
    },

    //在课程大纲详细信息填写界面，提交课程大纲 或 取消提交课程大纲时，返回课程大纲管理界面 并 清除大纲课程名、专业、年级信息
    backToClassPlanManage() {
      this.$emit('clearDataForClassPlan');
      this.$emit('toClassPlanManage');
    }
  }
}
</script>
  
<style>
.new_doc {
  height: 100%;
  width: 100%;
}

.new_doc .el-footer {
  height: 60px;
  border-top: 1px solid #93358c;
}
</style>
  