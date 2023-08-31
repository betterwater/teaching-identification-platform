<template>
	<div class="goal_and_request">
		<el-table class="table_for_goal_match_request" :data="this.GoalMatchRequest" border style="width:fit-content" max-height="700px">
			<el-table-column label="毕业要求" prop="requsetIdx" width="100px"></el-table-column>
			<el-table-column v-for="point in this.goals" :key="point" :label="point" :prop="point" width="100px">
				<template #default="scope">
					<button class="match_btn" @click="handleClick(scope.$index, point)">{{ scope.row[point] }}</button>
				</template>
			</el-table-column>
		</el-table>
	</div>
</template>
  
<script>
import { mapState, mapMutations } from 'vuex';

export default {
	name: 'GoalAndRequest',
	components: {

	},

	data() {
		return {
		}
	},

	computed: {
		...mapState(["tableDataCultivationGoal", "graduateRequestTable", "GoalMatchRequest", "goals", "initialGoalMatchRequest"]),
	},

	mounted() {
		if (this.initialGoalMatchRequest == 1) {
			this.getMatchTable();
			this.cleanInitialGoalMatchRequest();
		}
	},

	methods: {
		...mapMutations(["cleanInitialGoalMatchRequest"]),

		handleClick(key, kkey) {
			this.GoalMatchRequest[key][kkey] = Number(!this.GoalMatchRequest[key][kkey]);
		},
		getMatchTable() {
			//将培养目标名存入数组，方便向GoalMatchRequest下属对象中添加属性
			this.goals.length = 0;
			for (let key in this.tableDataCultivationGoal) {
				this.goals.push('培养目标' + (Number(key) + 1));
			}

			this.GoalMatchRequest.length = 0;
			for (var i = 0; i < this.graduateRequestTable.length; i++) {
				this.GoalMatchRequest.push({
					requsetIdx: '毕业要求' + (i + 1),
				})
			}
			
			for (let key in this.GoalMatchRequest) {
				for (let kkey in this.goals) {
					var newProperty = this.goals[kkey]
					this.GoalMatchRequest[key][newProperty] = 0
				}
			}

		}
	},
}
</script>
  
<style>
.match_btn {
	
	width: 100%;
	height: 100%;
	border: 0px;
	background-color: #FFFFFF;
	color: #93358c;
}
</style>
  