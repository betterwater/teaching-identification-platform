<template>
  <div class="loginSecond">

    <div class="login_head">
      <span>工程教育认证</span>
    </div>

    <div class="login_form">
      <el-form label-position="right" label-width="80px" size="default">

        <el-form-item label="账号:">
          <el-col :span="20">
            <el-input type="text" v-model="user" clearable="true" />
          </el-col>
        </el-form-item>

        <el-form-item label="密码:">
          <el-col :span="20">
            <el-input type="password" v-model="password" clearable="true" />
          </el-col>
        </el-form-item>

      </el-form>
    </div>

    <div class="login_btns">

      <button class="btn_in" @click="verifyIdentity">确认</button>
      <button class="btn_out" @click="switchToLoginFirst">取消</button>

    </div>

  </div>
</template>

<script>
import { ElForm } from 'element-plus'
import { ElFormItem } from 'element-plus'
import { ElInput } from 'element-plus'
import { ElCol } from 'element-plus'
import { login } from '../api/api.js'

export default {
  name: 'LoginSecond',
  components: {
    ElForm,
    ElFormItem,
    ElInput,
    ElCol,
  },

  data() {
    return {
      user: '',
      password: '',
      users: [],
    }
  },

  methods: {
    switchToLoginFirst() {
      this.user = ''
      this.password = ''
    },


    verifyIdentity() {
      if (this.user == '' || this.password == '') alert("用户名或密码不能为空")
      else {
        login(this.user, this.password).then(response => {
          if (response.data.code === "true") {
            this.$message({
              message: "登录成功",
              type: "success",
            });
            this.$parent.userName = response.data.userInfor.userName,
              this.$parent.userAccount = response.data.userInfor.userAccount,
              this.$parent.changePage()
          } else {
            this.$message({
              message: "用户名或密码错误",
              type: "error",
            });
          }
        })
      }
    }
  },
}
</script>

<style>
.loginSecond {
  width: 25%;
  position: absolute;
  top: 30%;
  right: 20%;
  padding: 30px;
  border-radius: 15px;
  text-align: center;
  background-color: #FFFFFF;
}

.login_head {
  position: relative;
  margin-bottom: 50px;
  font-size: xx-large;
  color: #93358c;
}

.login_form {
  position: relative;
  margin: 0 auto 50px auto;
  width: 90%;
}

.login_btns {
  position: relative;
  width: 50%;
  margin: auto;
  padding-left: 20px;
}

.btn_in {
  float: left;
  position: relative;
  padding: 5px 20px;
  border-radius: 5px;
  border: 1px solid #93358c;
  background-color: #FFFFFF;
  color: #93358c;
}

.btn_out {
  float: right;
  position: relative;
  padding: 5px 20px;
  border-radius: 5px;
  border: 1px solid #93358c;
  background-color: #FFFFFF;
  color: #93358c;
}

.btn_in:hover,
.btn_out:hover {
  background-color: #93358c;
  color: #FFFFFF;
}
</style>