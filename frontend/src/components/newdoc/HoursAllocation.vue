<template>
    <div class="edit_doc">
        <el-table :data="this.chapterData" stripe border style="width: fit-content;" max-height="700px">
            <el-table-column label="章节" width="200px">
                <template #default="scope">
                    {{ "第" + (Number(scope.$index) + 1) + "章 " + scope.row.chapterName }}
                </template>
            </el-table-column>
            <el-table-column prop="theoryHours" label="理论学时" width="145px">
                <template #default="{ row }">
                    <el-input-number size="small" controls-position="right" min="0" max="99" step="1" value-on-clear="min"
						v-model="row.theoryHours"></el-input-number>
                </template>
            </el-table-column>
            <el-table-column prop="practiceHours" label="实践学时" width="145px">
                <template #default="{ row }">
                    <el-input-number size="small" controls-position="right" min="0" max="99" step="1" value-on-clear="min"
						v-model="row.practiceHours"></el-input-number>
                </template>
            </el-table-column>
            <el-table-column prop="selfLearningHours" label="自主学习学时" width="145px">
                <template #default="{ row }">
                    <el-input-number size="small" controls-position="right" min="0" max="99" step="1" value-on-clear="min"
						v-model="row.selfLearningHours"></el-input-number>
                </template>
            </el-table-column>
            <el-table-column prop="description" label="说明" width="300px">
                <template #default="{ row }">
                    <el-input size="mini" v-model="row.description"></el-input>
                </template>
            </el-table-column>
        </el-table>
    </div>
</template>
  
<script>
import { mapState } from 'vuex';

export default {
    name: 'EditDoc',
    components: {

    },

    data() {
        return {

        }
    },

    computed: {
        ...mapState(["chapterData"]),
    },

    methods: {

    }
}
</script>
  
<style></style>