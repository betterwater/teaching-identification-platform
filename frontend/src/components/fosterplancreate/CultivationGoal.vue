<template>
	<div class="cultivation_goal">
		<p>1、专业描述</p>
		<el-input class="brief_info" v-model="subjectDescription" @change="updateSubjectDescription" :rows="6"
			type="textarea" placeholder="描述..." />
		<p>2、培养目标</p>
		<div class="cultivation_goal_scrollbar">
			<el-table :data="tableDataCultivationGoal" :index="indexMethod" stripe border style="width:fit-content">
				<el-table-column type="index" label="序号" width="100px" />
				<el-table-column prop="CultivationGoal" label="培养要求" width="100px" />
				<el-table-column prop="description" label="描述" width="600px" :show-overflow-tooltip="true" />
				<el-table-column prop="" label="操作" width="110px">
					<template #default="scope">
						<button class="goal_btn" @click="deleteCultivationGoalItem(scope.$index)"
							style="margin-right:5px">删除</button>
						<button class="goal_btn"
							@click="editCultivationGoalItem(scope.$index, scope.row); CultivationGoalDialogVisible = true">编辑</button>
					</template>
				</el-table-column>
			</el-table>
			<button class="add_cultivation_require_item_btn" @click="addCultivationGoalItem">添加</button>
		</div>

		<!-- 培养要求修改表单 -->
		<el-dialog v-model="CultivationGoalDialogVisible" title="培养要求">
			<el-form ref="form" :model="currentRow" label-width="auto">
				<el-form-item label="培养要求">
					<el-input v-model="currentRow.CultivationGoal"></el-input>
				</el-form-item>
				<el-form-item label="描述">
					<el-input v-model="currentRow.description" :rows="4" type="textarea" placeholder="描述..."></el-input>
				</el-form-item>
			</el-form>
			<div style="text-align: center;">
				<el-button @click="CultivationGoalDialogVisible = false">取消</el-button>
				<el-button type="primary" @click="saveCultivationGoalItem">保存</el-button>
			</div>
		</el-dialog>
	</div>
</template>
  
<script>
import { mapState, mapMutations } from 'vuex';

export default {
	name: 'CultivationGoal',
	components: {

	},

	data() {
		return {
			//专业培养目标及要求：当前修改行、培养要求修改表单是否显示、专业描述、培养目标数据
			currentRow: {},
			CultivationGoalDialogVisible: false,
			subjectDescription: '',
			//当前编辑的培养目标的index
			goalIndex: -1,
		}
	},

	computed: {
		...mapState(["subjectDescriptionStore", "tableDataCultivationGoal"]),
	},

	mounted() {
		this.subjectDescription = this.subjectDescriptionStore;
	},

	methods: {
		...mapMutations(["updateSubjectDescriptionStore", "setInitialGoalMatchRequest"]),

		//专业描述对应的更新方法
		updateSubjectDescription() {
			this.updateSubjectDescriptionStore(this.subjectDescription)
		},

		//添加培养目标
		addCultivationGoalItem() {
			this.tableDataCultivationGoal.push({
				CultivationGoal: '培养要求',
				description: '描述'
			})
			this.setInitialGoalMatchRequest();
		},

		//删除培养目标
		deleteCultivationGoalItem(index) {
			this.tableDataCultivationGoal.splice(index, 1);
			this.setInitialGoalMatchRequest();
		},

		//编辑培养目标
		editCultivationGoalItem(index, row) {
			this.goalIndex = index
			this.currentRow = Object.assign({}, row);
		},

		//保存编辑内容
		saveCultivationGoalItem() {
			Object.assign(this.tableDataCultivationGoal[this.goalIndex], this.currentRow);
			this.CultivationGoalDialogVisible = false;
		},

		indexMethod(index) {
			return index + 1;
		},

	}
}
</script>
  
<style>
.cultivation_goal_scrollbar {
    width: fit-content;
    height: 500px;
    overflow-y: auto;
}

.cultivation_goal_scrollbar::-webkit-scrollbar {
    width: 8px;
}

.cultivation_goal_scrollbar::-webkit-scrollbar-thumb {
    background-color: #ccc;
}

.cultivation_goal_scrollbar::-webkit-scrollbar-thumb:hover {
    background-color: #aaa;
}
</style>
  