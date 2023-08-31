<template>
    <div class="course_weight">
        <el-table :data="this.CourseMatchRequest" border style="width: fit-content;" max-height="700px">
            <el-table-column label="课程名称" prop="courseName" width="100px"></el-table-column>
            <el-table-column v-for="point in this.indicatorPoints" :key="point" :label="'指标点' + point" :prop="point"
                width="100px">
                <template #default="scope">
                    <el-input-number size="small" style="width: 75px;" controls-position="right" min="0" max="1" step="0.1" value-on-clear="min"
						v-model="scope.row[point]"></el-input-number>
                </template>
            </el-table-column>
        </el-table>
    </div>
</template>
  
<script>
import { ElTableColumn } from 'element-plus';
import { mapState, mapMutations } from 'vuex';

export default {
    name: 'CourseWeight',
    components: {
        ElTableColumn
    },

    data() {
        return {
        }
    },

    computed: {
        ...mapState(["tableCourseInFosterplan", "graduateRequestTable", "CourseMatchRequest", "indicatorPoints", "initialCourseMatchRequest"]),
    },

    mounted() {
        if (this.initialCourseMatchRequest == 1) {
            this.getCourseMatchRequestTable();
            this.cleanInitialCourseMatchRequest();
        }
    },

    methods: {
        ...mapMutations(["cleanInitialCourseMatchRequest"]),

        //生成课程与毕业指标点对应数据
        getCourseMatchRequestTable() {
            //将毕业指标点放入数组，方便向CourseMatchRequest中 添加属性
            this.indicatorPoints.length = 0;
            for (let key in this.graduateRequestTable) {
                for (let kkey in this.graduateRequestTable[key].points) {
                    this.indicatorPoints.push((Number(key) + 1) + '-' + (Number(kkey) + 1))
                }
            }

            this.CourseMatchRequest.length = 0;
            for (let key in this.tableCourseInFosterplan) {
                this.CourseMatchRequest.push({
                    courseName: this.tableCourseInFosterplan[key].courseName,
                })
            }

            for (let key in this.CourseMatchRequest) {
                for (let kkey in this.indicatorPoints) {
                    var newProperty = this.indicatorPoints[kkey]
                    this.CourseMatchRequest[key][newProperty] = 0
                }
            }
        },
    }
}
</script>
  
<style></style>
  