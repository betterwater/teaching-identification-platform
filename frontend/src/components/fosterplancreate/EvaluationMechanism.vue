<template>
  <div class="evaluation_mechanism">
    <el-input class="brief_info" v-model="evaluationMechanism" @change="updateEvaluationMechanism" clearable="true"
      :rows="8" type="textarea" placeholder="请输入评价机制"></el-input>
  </div>
</template>
  
<script>
import { ElInput } from 'element-plus';
import { mapState, mapMutations } from 'vuex';

export default {
  name: 'EvaluationMechanism',
  components: {
    ElInput
  },

  data() {
    return {
      evaluationMechanism: ''
    }
  },

  computed: {
    ...mapState(["evaluationMechanismStore"]),
  },

  mounted() {
    this.evaluationMechanism = this.evaluationMechanismStore
  },

  methods: {
    ...mapMutations(["updateEvaluationMechanismStore"]),

    updateEvaluationMechanism() {
      this.updateEvaluationMechanismStore(this.evaluationMechanism);
    }
  }
}
</script>
  
<style></style>
  