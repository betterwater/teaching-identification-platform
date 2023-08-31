<template>
	<div class="course_and_request">
		<el-table :data="this.CourseSupportRequest" border style="width: fit-content;" max-height="700px">
			<el-table-column label="课程名称" prop="courseName" width="100px"></el-table-column>
			<el-table-column v-for="point in this.requests" :key="point" :label="'毕业要求' + point" :prop="point"
				width="120px">
				<template #default="scope">
					<el-select v-model="scope.row[point]" clearable="true" placeholder="空">
						<el-option v-for="item in AllOptions" :key="item.support" :label="item.support"
							:value="item.support" />
					</el-select>
				</template>
			</el-table-column>
		</el-table>
	</div>
</template>
  
<script>
import { ElTableColumn } from 'element-plus';
import { mapState, mapMutations } from 'vuex';

export default {
	name: 'CourseAndRequest',
	components: {
		ElTableColumn,
	},

	data() {
		return {
			AllOptions: [
				{
					support: 'H'
				},
				{
					support: 'M'
				},
				{
					support: 'L'
				}
			]
		}
	},

	computed: {
		...mapState(["tableCourseInFosterplan", "graduateRequestTable", "CourseSupportRequest", "requests", "initialCourseSupportRequest"]),
	},

	mounted() {
		if (this.initialCourseSupportRequest == 1) {
			this.getCourseSupportRequestTable();
			this.cleanInitialCourseSupportRequest();
		}
	},

	methods: {
		...mapMutations(["cleanInitialCourseSupportRequest"]),

		getCourseSupportRequestTable() {
			//将毕业要求名放入数组，方便向CourseSupportRequest中添加属性
			this.requests.length = 0;
			for (let key in this.graduateRequestTable) {
				this.requests.push(Number(key) + 1)
			}

			this.CourseSupportRequest.length = 0;
			for (let key in this.tableCourseInFosterplan) {
				this.CourseSupportRequest.push({
					courseName: this.tableCourseInFosterplan[key].courseName,
				})
			}
			for (let key in this.CourseSupportRequest) {
				for (let kkey in this.requests) {
					var newProperty = this.requests[kkey]
					this.CourseSupportRequest[key][newProperty] = ''
				}
			}
		},

	}
}
</script>
  
<style></style>
  