<template>
  <div class="education">

    <el-container class="layout_container">
      <el-header>
        <el-menu mode="horizontal" background-color="#93358c" text-color="#FFFFFF" active-text-color="#FFFFFF"
          default-active="1">

          <div>
            <el-menu-item @click="changeToRegister">
              <p class="logo">工程教育认证</p>
            </el-menu-item>
          </div>

          <el-menu-item index="1" @click="showAsideMenu(1)">培养方案</el-menu-item>
          <el-menu-item index="2" @click="showAsideMenu(2)">课程管理</el-menu-item>
          <el-menu-item index="3" @click="showAsideMenu(3)">毕业要求</el-menu-item>
          <div class="main_account">{{ userName }}</div>
        </el-menu>
      </el-header>

      <el-container class="sideways">
        <el-aside width="245px">
          <el-menu v-if="this.asideMenuIndex == '1'" default-active="1-1">
            <el-menu-item class="aside_menu_item" index="1-1" @click="showMainComponent('1-1')" ref="toFosterPlanAll">
              <div class="aside_menu_item_bg"></div>方案总览
            </el-menu-item>
            <el-menu-item class="aside_menu_item" index="1-2" @click="showMainComponent('1-2')">
              <div class="aside_menu_item_bg"></div>创建方案
            </el-menu-item>
          </el-menu>

          <el-menu v-if="this.asideMenuIndex == '2'" default-active="2-1">
            <el-menu-item class="aside_menu_item" index="2-1" @click="showMainComponent('2-1')">
              <div class="aside_menu_item_bg"></div>大纲管理
            </el-menu-item>
            <el-menu-item class="aside_menu_item" index="2-2" @click="showMainComponent('2-2')">
              <div class="aside_menu_item_bg"></div>大纲总览
            </el-menu-item>
            <el-menu-item class="aside_menu_item" index="2-3" @click="showMainComponent('2-3')">
              <div class="aside_menu_item_bg"></div>课程分析
            </el-menu-item>
          </el-menu>

          <el-menu v-if="this.asideMenuIndex == '3'" default-active="3-1">
            <el-menu-item class="aside_menu_item" index="3-1" @click="showMainComponent('3-1')">
              <div class="aside_menu_item_bg"></div>毕业要求
            </el-menu-item>
          </el-menu>
        </el-aside>

        <el-main>
          <FosterPlanCreate v-if="this.mainComponentIndex == '1-2'" @toFosterPlanAll="toFosterPlanAll()">
          </FosterPlanCreate>
          <FosterPlanAll v-else-if="this.mainComponentIndex == '1-1'"></FosterPlanAll>
          <ClassPlanCreate v-else-if="this.mainComponentIndex == '2-1'"></ClassPlanCreate>
          <ClassPlanAll v-else-if="this.mainComponentIndex == '2-2'"></ClassPlanAll>
          <ClassPlanAnalyse v-else-if="this.mainComponentIndex == '2-3'"></ClassPlanAnalyse>
          <GraduateRequest v-else-if="this.mainComponentIndex == '3-1'"></GraduateRequest>
        </el-main>

      </el-container>
    </el-container>
  </div>
</template>

<script>
import { ElContainer, ElHeader, ElAside, ElMain, ElMenu, ElMenuItem } from 'element-plus';
import FosterPlanCreate from './components/FosterPlanCreate.vue'
import FosterPlanAll from './components/FosterPlanAll.vue'
import ClassPlanCreate from './components/ClassPlanCreate.vue'
import ClassPlanAll from './components/ClassPlanAll.vue'
import ClassPlanAnalyse from './components/ClassPlanAnalyse.vue'
import GraduateRequest from './components/GraduateRequest.vue'

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: 'Education',
  components: {
    FosterPlanCreate,
    FosterPlanAll,
    ClassPlanCreate,
    ClassPlanAll,
    ClassPlanAnalyse,
    GraduateRequest,
    ElContainer,
    ElHeader,
    ElAside,
    ElMain,
    ElMenu,
    ElMenuItem,
  },

  data() {
    return {
      asideMenuIndex: '1',
      mainComponentIndex: '1-1',
      userName: '',
      userAccount: '',
      globalData: {
        name: '',
        account: '',
      }
    }
  },

  provide() {
    return {
      globalData: this.globalData
    }
  },

  methods: {
    changeToRegister() {
      this.$router.push('/app')
    },

    showAsideMenu(num) {
      if (this.asideMenuIndex != num) {
        this.asideMenuIndex = num;
        this.mainComponentIndex = num + '-' + '1';
      }
    },

    showMainComponent(str) {
      this.mainComponentIndex = str;
    },

    //培养方案提交或取消提交时，回到方案总览界面
    toFosterPlanAll() {
      this.$refs.toFosterPlanAll.$el.click();
    }
  },

  mounted() {
    this.userName = this.$route.query.userName
    this.userAccount = this.$route.query.userAccount
    this.globalData.name = this.userName
    this.globalData.account = this.userAccount
  }

}
</script>

<style>
.education {
  height: 100%;
  width: 100%;
  position: fixed;
  background-color: #FFFFFF;
}

.main_account {
  margin-left: auto;
  font-size: 22px;
  color: white;
  margin-right: 40px;
  display: flex;
  align-items: center;
}

.sideways {
  margin-top: 10px;
}

.layout_container {
  height: 100%;
  width: 100%;
}

.layout_container .el-header {
  padding: 0px;
  background-color: #93358c;
}

.layout_container .el-header .el-menu--horizontal {
  border-bottom: 0;
}

.logo {
  font-size: 26px;
  font-weight: bolder;
  margin: auto;
  padding-left: 25px;
  padding-right: 25px;
}

.layout_container .el-header .el-menu-item {
  font-size: 22px;
  margin-right: 50px;
}

.aside_menu_item {
  box-shadow: 0 0 1px #93358c inset;
  border-radius: 3px;
  color: black !important;
  font-weight: 700;
  font-size: 18px;
  padding-left: 0px !important;
  margin-top: 5px;
  margin-bottom: 15px;
}

.aside_menu_item.is-active .aside_menu_item_bg {
  background-color: #93358c;
}

.aside_menu_item_bg {
  width: 12px;
  height: 55px;
  margin-right: 15px;
  border-radius: 3px 0px 0px 3px;
  background-color: #d2b5d0;
}

.el-main {
  padding: 5px 0 0 20px !important;
}
</style>