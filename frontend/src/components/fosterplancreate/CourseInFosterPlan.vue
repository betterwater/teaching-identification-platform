<template>
	<div class="course_in_fosterplan">
		<el-table :data="tableCourseInFosterplan" stripe border style="width:1000px">
			<el-table-column type="index" v-if="false"></el-table-column>
			<!-- <el-table-column prop="courseCode" label="课程代码" width="100px">
				<template #default="{ row }">
					<el-input size="mini" v-model="row.courseCode"></el-input>
				</template>
			</el-table-column> -->
			<el-table-column prop="courseName" label="课程名称" width="180px">
				<template #default="{ row }">
					<el-input size="mini" v-model="row.courseName"></el-input>
				</template>
			</el-table-column>
			<el-table-column prop="courseCategory" label="课程类别" width="180px">
				<template #default="{ row }">
					<el-select size="mini" v-model="row.courseCategory" placeholder="请选择课程类别">
						<el-option v-for="item in courseCategoryOptions" :key="item.index" :label="item.label"
							:value="item.label">
						</el-option>
					</el-select>
				</template>
			</el-table-column>
			<el-table-column prop="credits" label="总学分" width="145px">
				<template #default="{ row }">
					<el-input-number size="small" controls-position="right" min="0" max="10" step="1" value-on-clear="min"
						v-model="row.credits"></el-input-number>
				</template>
			</el-table-column>
			<el-table-column prop="hours" label="总学时" width="145px">
				<template #default="{ row }">
					<el-input-number size="small" controls-position="right" min="0" max="100" step="1" value-on-clear="min"
						v-model="row.hours"></el-input-number>
				</template>
			</el-table-column>
			<el-table-column prop="semester" label="开课学期" width="150px">
				<template #default="{ row }">
					<el-select size="mini" v-model="row.semester" placeholder="请选择学期">
						<el-option v-for="item in semesterOptions" :key="item.index" :label="item.label"
							:value="item.label">
						</el-option>
					</el-select>
				</template>
			</el-table-column>
			<el-table-column prop="isRequired" label="课程性质" width="100px">
				<template #default="{ row }">
					<el-select size="mini" v-model="row.isRequired" placeholder=" ">
						<el-option v-for="item in isRequiredOptions" :key="item.index" :label="item.label"
							:value="item.label">
						</el-option>
					</el-select>
				</template>
			</el-table-column>
			<el-table-column prop="" label="操作" width="100px">
				<template #default="scope">
					<button class="goal_btn" @click="deleteCourseInFosterplan(scope.$index)"
						style="margin-right:5px">删除</button>
				</template>
			</el-table-column>
		</el-table>
		<button class="goal_btn add_course_in_fosterplan_btn" @click="addCourseInFosterplan">添加</button>
	</div>
</template>
  
<script>
import { mapState, mapMutations } from 'vuex';

export default {
	name: 'CourseInFosterPlan',
	components: {

	},

	data() {
		return {

			//课程类别
			courseCategoryOptions: [
				{
					index: 0,
					label: '专业基础课程',
				},
				{
					index: 1,
					label: '专业类课程',
				},
				{
					index: 2,
					label: '工程基础类课程',
				},
				{
					index: 3,
					label: '工程实践与毕业设计',
				},
				{
					index: 4,
					label: '数学与自然科学课程',
				},
				{
					index: 5,
					label: '人类社会科学类通识教育课程',
				},
			],

			//开课学期
			semesterOptions: [
				{
					index: 0,
					label: '第一学年上',
				},
				{
					index: 1,
					label: '第一学年下',
				},
				{
					index: 2,
					label: '第二学年上',
				},
				{
					index: 3,
					label: '第二学年下',
				},
				{
					index: 4,
					label: '第三学年上',
				},
				{
					index: 5,
					label: '第三学年下',
				},
				{
					index: 6,
					label: '第四学年上',
				},
				{
					index: 7,
					label: '第四学年下',
				},
				{
					index: 8,
					label: '短学期1',
				},
				{
					index: 9,
					label: '短学期2',
				},
			],

			//课程性质
			isRequiredOptions: [
				{
					index: 0,
					label: '必修'
				},
				{
					index: 1,
					label: '选修'
				},
			]
		}
	},

	computed: {
		...mapState(["tableCourseInFosterplan"]),
	},

	methods: {
		...mapMutations(["setInitialCourseSupportRequest", "setInitialCourseMatchRequest"]),

		//删除一门课程
		deleteCourseInFosterplan(index) {
			this.tableCourseInFosterplan.splice(index, 1);
			this.setInitialCourseSupportRequest();
			this.setInitialCourseMatchRequest();
		},

		//添加一门课程
		addCourseInFosterplan() {
			this.tableCourseInFosterplan.push({
				// courseCode: '',
				courseName: '',
				courseCategory: '',
				credits: '',
				hours: '',
				semester: '',
				isRequired: '',
			})
			this.setInitialCourseSupportRequest();
			this.setInitialCourseMatchRequest();
		},
	}
}
</script>
  
<style>
.add_course_in_fosterplan_btn {
	width: 1000px;
	margin-top: 10px;
}

.course_in_fosterplan {
    width: fit-content;
    height: 700px;
    overflow-y: auto;
}

.course_in_fosterplan::-webkit-scrollbar {
    width: 8px;
}

.course_in_fosterplan::-webkit-scrollbar-thumb {
    background-color: #ccc;
}

.course_in_fosterplan::-webkit-scrollbar-thumb:hover {
    background-color: #aaa;
}
</style>
  