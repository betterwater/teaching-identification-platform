<template>
    <div class="create_course_outline">
        <p>
            <span class="info_item">课程名：{{ this.newClassNameStore }}</span>
            <span class="info_item">开课专业：{{ this.newClassSubjectStore }}</span>
            <span class="info_item">适用年级：{{ this.newClassYearStore }}</span>
            <span class="info_item">课程性质：{{ this.isRequired }}</span>
        </p>
        <p>
            <span class="info_item">课程类别：{{ this.Category }}</span>
            <span class="info_item">总学分：{{ this.credits }}</span>
            <span class="info_item">总学时：{{ this.hours }}</span>
            <span class="info_item">开课学期：{{ this.semester }}</span>
        </p><br /><br />

        <span>课程简介：</span><br />
        <el-input class="brief_info" v-model="courseBriefInfo" @change="updateCourseBriefInfo" :rows="8" type="textarea"
            placeholder="简介..." />
    </div>
</template>
  
<script>
import { mapState, mapMutations } from 'vuex';
import { getCourse } from '../../api/api.js'
export default {
    name: 'CreateCourseOutline',
    components: {

    },

    data() {
        return {
            //课程基本信息
            // className: '',
            // subject: '',
            // year: '',
            isRequired: '',
            Category: '',
            credits: '',
            hours: '',
            semester: '',

            //课程简介
            courseBriefInfo: '',
        }
    },

    computed: {
        ...mapState(["newClassNameStore", "newClassSubjectStore", "newClassYearStore", "courseBriefInfoStore"]),
    },

    mounted() {
        this.courseBriefInfo = this.courseBriefInfoStore
        getCourse(this.newClassSubjectStore, this.newClassNameStore, this.newClassYearStore).then(response => {
            console.log(response.data);
            this.isRequired = response.data.content[0].isRequired
            this.Category = response.data.content[0].courseCategory
            this.credits = response.data.content[0].credits
            this.hours = response.data.content[0].hours
            this.semester = response.data.content[0].semester
        })
    },

    methods: {
        ...mapMutations(["updateCourseBriefInfoStore"]),
        
        updateCourseBriefInfo() {
            this.updateCourseBriefInfoStore(this.courseBriefInfo);
        }
    }
}
</script>
  
<style>
.info_item {
    margin-right: 20px;
    width: 200px;
    display: inline-block;
}
</style>