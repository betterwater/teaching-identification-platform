<template>
	<div class="add_graduate_request">
		<div class="formOuterBox" v-for="(item, index) in graduateRequestTable" :key="index">
			<div class="formContentBox">
				<h4>毕业要求 {{ index + 1 }}</h4>
				<!-- 毕业要求表单内容 -->
				<!-- eslint-disable-next-line -->
				<el-form @submit.native.prevent>
					<!-- 毕业要求填写 -->
					<el-form-item>
						<el-input :rows="3" type="textarea" placeholder="内容..." v-model="item.info"></el-input>
					</el-form-item>
					<!-- 毕业指标点表格 -->
					<el-table :data="item.points" :index="indexMethod" stripe border>
						<el-table-column type="index" label="序号" width="100px" />
						<el-table-column prop="point" label="指标点" width="380px" :show-overflow-tooltip="true" />
						<el-table-column prop="" label="操作" width="120px">
							<template #default="scope">
								<button class="goal_btn"
									@click="editGraduatePoint(index, scope.row, scope); graduatePointDialogVisible = true">编辑</button>
								<button class="goal_btn" style="margin-left:5px" v-if="item.points.length > 1"
									@click="deleteGraduatePoint(item, scope)">删除</button>
							</template>
						</el-table-column>
					</el-table>
					<!-- 添加毕业指标点 -->
					<button class="add_graduate_point_btn" @click="addGraduatePoint(item)">添加</button>
				</el-form>
				<!-- 编辑毕业指标点 -->
				<el-dialog v-model="graduatePointDialogVisible" title="培养要求">
					<el-form ref="form" :model="currentPoint">
						<el-form-item label="指标点">
							<el-input v-model="currentPoint.point"></el-input>
						</el-form-item>
					</el-form>
					<div>
						<el-button @click="graduatePointDialogVisible = false">取消</el-button>
						<el-button type="primary" @click="saveGraduatePoint()">保存</el-button>
					</div>
				</el-dialog>

			</div>
			<!-- 添加毕业要求 -->
			<div>
				<el-button v-if="index == graduateRequestTable.length - 1" @click="addForm"
					type="success">添加毕业要求</el-button>
				<el-button v-if="graduateRequestTable.length > 1" @click="removeIdx(index)"
					type="danger">删除此条毕业要求</el-button>
			</div>
		</div>
	</div>
</template>
  
<script>
import { mapState, mapMutations } from 'vuex';

export default {
	name: 'GraduateRequest',
	components: {

	},

	data() {
		return {
			//毕业要求数据
			// graduateRequestTable: [
			// 	{
			// 		info: "",
			// 		points: [
			// 			{
			// 				point: '',
			// 			},
			// 		]
			// 	},
			// ],

			graduatePointDialogVisible: false,//控制指标点编辑表单显示
			currentPoint: {},//当前编辑毕业指标点
			currentIdx: -1,//当前编辑毕业指标点下标
			currentRequestIdx: -1,//当前编辑毕业要求下标
		}
	},

	computed: {
		...mapState(["graduateRequestTable"]),
	},

	methods: {
		...mapMutations(["setInitialGoalMatchRequest", "setInitialCourseSupportRequest", "setInitialCourseMatchRequest"]),

		addForm() {
			// 定义一个标识，通过标识判断是否能添加信息
			let statusType = true;
			this.graduateRequestTable.forEach((item) => {
				if (
					item.info == ""
				) {
					this.$message({
						message: "请补充当前毕业要求内容后再添加新毕业要求",
						type: "warning",
					});
					statusType = false;
				}
			});
			if (statusType) {
				this.graduateRequestTable.push({
					info: "",
					points: [
						{
							point: '',
						},
					]
				});
				this.setInitialGoalMatchRequest();
				this.setInitialCourseSupportRequest();
				this.setInitialCourseMatchRequest();
			}
		},
		// 删除操作
		removeIdx(index) {
			this.graduateRequestTable.splice(index, 1);
			this.setInitialGoalMatchRequest();
			this.setInitialCourseSupportRequest();
			this.setInitialCourseMatchRequest();
			this.$message({
				message: "删除成功",
				type: "success",
			});
		},

		//添加毕业指标点
		addGraduatePoint(item) {
			item.points.push({
				point: '',
			})
			this.setInitialCourseMatchRequest();
		},

		//删除毕业指标点
		deleteGraduatePoint(item, scope) {
			item.points.splice(scope.$index, 1);
			this.setInitialCourseMatchRequest();
		},

		//编辑毕业指标点
		editGraduatePoint(index, row, scope) {
			this.currentPoint = Object.assign({}, row);
			this.currentIdx = scope.$index;
			this.currentRequestIdx = index;
		},

		//保存编辑内容
		saveGraduatePoint() {
			Object.assign(this.graduateRequestTable[this.currentRequestIdx].points[this.currentIdx], this.currentPoint);
			this.graduatePointDialogVisible = false;
		},

		//毕业指标点index生成
		indexMethod(index) {
			return index + 1;
		}
	}
}
</script>
  
<style>
.add_graduate_request {
	width: 680px;
	height: 700px;
	overflow-y: auto;
}

.add_graduate_request::-webkit-scrollbar {
	width: 12px;
}

.add_graduate_request::-webkit-scrollbar-thumb {
	background-color: #ccc;
}

.add_graduate_request::-webkit-scrollbar-thumb:hover {
	background-color: #aaa;
}

.addFormBox {
	margin: 20px;
}

.formOuterBox {
	width: 600px;
	margin-bottom: 20px;
	padding: 15px 20px;
	border: 1px solid #D3D3D3;
	border-radius: 10px;
	box-shadow: 0 0 15px #D3D3D3;
}

h4 {
	margin: 0px 0px 10px 0px;
}

.add_graduate_point_btn {
	margin-top: 10px;
	margin-bottom: 10px;
	width: 600px;
	border-radius: 3px;
	border: 1px solid #93358c;
	background-color: #FFFFFF;
	color: #93358c;
}

.add_graduate_point_btn:hover {
	background-color: #93358c;
	color: #FFFFFF;
}
</style>
  