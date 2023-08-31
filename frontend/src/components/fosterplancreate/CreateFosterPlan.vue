<template>
	<div class="create_foster_plan">
		<el-input class="foster_plan_name" v-model="facility" @change="updateFacility" clearable="true"
			placeholder="请输入学院名称"></el-input>
		<el-input class="foster_plan_name" v-model="subject" @change="updateSubject" clearable="true"
			placeholder="请输入专业名称"></el-input>
		<el-input class="foster_plan_name" v-model="year" @change="updateYear" clearable="true"
			placeholder="请输入适用年级"></el-input>
		<el-input class="brief_info" v-model="briefInfo" @change="updateBriefInfo" :rows="8" type="textarea"
			placeholder="简介..." />
	</div>
</template>
  
<script>

import { mapState, mapMutations } from 'vuex';

export default {
	name: 'CreateFosterPlan',
	components: {

	},

	data() {
		return {
			//培养方案创建：学院、专业、年级、简介
			facility: '',
			subject: '',
			year: '',
			briefInfo: '',
		}
	},

	computed: {
		...mapState(["facilityStore", "subjectStore", "yearStore", "briefInfoStore"]),
	},

	mounted() {
		this.facility = this.facilityStore;
		this.subject = this.subjectStore;
		this.year = this.yearStore;
		this.briefInfo = this.briefInfoStore;
	},

	methods: {
		...mapMutations(["updateFacilityStore", "updateSubjectStore", "updateYearStore", "updateBriefInfoStore"]),

		//培养方案创建：学院、专业、年级、简介对应的更新方法
		updateFacility() {
			this.updateFacilityStore(this.facility);
		},

		updateSubject() {
			this.updateSubjectStore(this.subject);
		},

		updateYear() {
			this.updateYearStore(this.year);
		},

		updateBriefInfo() {
			this.updateBriefInfoStore(this.briefInfo);
		}
	}
}
</script>
  
<style></style>
  