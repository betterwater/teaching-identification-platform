<template>
    <div class="edit_doc">
        <div class="edit_assessment_method">
            <el-table :data="this.courseGoalTable" stripe border style="width: 555px;">
                <el-table-column label="课程目标" width="120px">
                    <template #default="scope">
                        {{ "课程目标" + Number(scope.$index + 1) }}
                    </template>
                </el-table-column>
                <el-table-column prop="homeworkRatio" label="作业分数占比" width="145px">
                    <template #default="{ row }">
                        <el-input-number size="small" controls-position="right" min="0" max="1" step="0.1"
                            value-on-clear="min" v-model="row.homeworkRatio"></el-input-number>
                    </template>
                </el-table-column>
                <el-table-column prop="examRatio" label="考试分数占比" width="145px">
                    <template #default="{ row }">
                        <el-input-number size="small" controls-position="right" min="0" max="1" step="0.1"
                            value-on-clear="min" v-model="row.examRatio"></el-input-number>
                    </template>
                </el-table-column>
                <el-table-column prop="experienceRatio" label="实验分数占比" width="145px">
                    <template #default="{ row }">
                        <el-input-number size="small" controls-position="right" min="0" max="1" step="0.1"
                            value-on-clear="min" v-model="row.experienceRatio"></el-input-number>
                    </template>
                </el-table-column>
            </el-table>
        </div>
    </div>
</template>
  
<script>
import { mapState } from 'vuex';
import { ElTable } from 'element-plus';

export default {
    name: 'EditDoc',
    components: {
        ElTable
    },

    data() {
        return {

        }
    },

    computed: {
        ...mapState(["courseGoalTable"]),
    },

    methods: {
    }
}
</script>
  
<style>
.edit_assessment_method {
    width: 570px;
    height: 700px;
    overflow-y: auto;
}

.edit_assessment_method::-webkit-scrollbar {
    width: 8px;
}

.edit_assessment_method::-webkit-scrollbar-thumb {
    background-color: #ccc;
}

.edit_assessment_method::-webkit-scrollbar-thumb:hover {
    background-color: #aaa;
}
</style>