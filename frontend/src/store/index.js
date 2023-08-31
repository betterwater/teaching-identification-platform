import { createStore } from 'vuex'

export default createStore({
	state: {
		//1、培养方案创建：学院、专业、年级、简介
		facilityStore: '',
		subjectStore: '',
		yearStore: '',
		briefInfoStore: '',

		//2、专业培养目标及要求：专业描述、培养目标表格
		subjectDescriptionStore: '',
		tableDataCultivationGoal: [
			{
				CultivationGoal: '培养要求',
				description: '描述'
			}
		],

		//3、毕业要求及指标点
		graduateRequestTable: [
			{
				info: "",
				points: [
					{
						point: '',
					},
				]
			},
		],

		//4、培养目标与毕业要求对应表
		GoalMatchRequest: [
			// {
			// 	requsetIdx:毕业要求1,
			// 	培养目标1:0,
			//  培养目标2:1,
			// },
		],
		initialGoalMatchRequest: 1,//GoalMatchRequest是否需要初始化
		goals: [],//辅助数组，放置培养目标名

		//5、教学计划表
		tableCourseInFosterplan: [
			{
				// courseCode: 'soft000',
				courseName: '课程名称',
				courseCategory: '专业基础课程',
				credits: '0',
				hours: '0',
				semester: '第一学年上',
				isRequired: '必修',
			},
		],

		//6、课程权重（课程对每个毕业指标点的贡献）
		CourseMatchRequest: [
			// {
			// 	courseName: '课程名称',
			// 	'1-1':0
			// },
		],
		initialCourseMatchRequest: 1,//CourseMatchRequest是否需要初始化
		indicatorPoints: [],//辅助数组，放置毕业指标点

		//7、课程对毕业要求支撑关系
		CourseSupportRequest: [
			// {
			// 	courseName:'',
			// 	'1':'',
			// }
		],
		initialCourseSupportRequest: 1,//CourseSupportRequest是否需要初始化
		requests: [],//辅助数组，放置毕业要求名

		//8、评价机制
		evaluationMechanismStore: '',

		//课程大纲创建
		//1、课程名、专业、适用年级、课程简介
		newClassNameStore: '',
		newClassSubjectStore: '',
		newClassYearStore: '',
		courseBriefInfoStore: '',

		//2、课程章节知识点添加 3、课程章节学时分配
		chapterData: [
			{
				chapterName: '',
				//理论学时、实践学时、自主学习学时、说明
				theoryHours: 0,
				practiceHours: 0,
				selfLearningHours: 0,
				description: '',
				keyPoints: [
					{
						keyPoint: '',
					},
				]
			},
		],

		//4、课程目标添加:课程目标表，课程目标对毕业指标点权重表
		courseGoalTable: [
			{
				goal: '',
				pointIndex: [
					// '1-1',
					// '2-1'
				],
				homeworkRatio: 0,
				examRatio: 0,
				experienceRatio: 0
			},
		],

		courseGoalWeightTable: [
			// {
			// 	pointIndex:'',
			// 	courseGoalIndex:'',
			//  courseGoal:'',
			//  weight:''
			// },
		],
	},
	mutations: {
		// addCultivationGoalItemStore(state, item) {
		// 	state.tableDataCultivationGoal.push(item)
		// },

		//培养方案创建：学院、专业、年级、简介对应的更新方法
		updateFacilityStore(state, str) {
			state.facilityStore = str;
		},
		updateSubjectStore(state, str) {
			state.subjectStore = str;
		},
		updateYearStore(state, str) {
			state.yearStore = str;
		},
		updateBriefInfoStore(state, str) {
			state.briefInfoStore = str;
		},

		//专业培养目标及要求：专业描述对应的更新方法
		updateSubjectDescriptionStore(state, str) {
			state.subjectDescriptionStore = str;
		},

		//培养目标与毕业要求对应表，辅助参数initialGoalMatchRequest的更新方法
		setInitialGoalMatchRequest(state) {
			state.initialGoalMatchRequest = 1
		},

		cleanInitialGoalMatchRequest(state) {
			state.initialGoalMatchRequest = 0
		},

		//课程权重，辅助参数initialCourseMatchRequest的更新方法
		setInitialCourseMatchRequest(state) {
			state.initialCourseMatchRequest = 1
		},

		cleanInitialCourseMatchRequest(state) {
			state.initialCourseMatchRequest = 0
		},

		//课程对毕业要求支撑关系，辅助参数initialCourseSupportRequest的更新方法
		setInitialCourseSupportRequest(state) {
			state.initialCourseSupportRequest = 1
		},

		cleanInitialCourseSupportRequest(state) {
			state.initialCourseSupportRequest = 0
		},

		//评价机制：评价机制对应的更新方法
		updateEvaluationMechanismStore(state, str) {
			state.evaluationMechanismStore = str;
		},

		//培养方案创建完成后清除数据项
		cleanFosterPlan(state) {
			//1、培养方案创建：学院、专业、年级、简介
			state.facilityStore = ''
			state.subjectStore = ''
			state.yearStore = ''
			state.briefInfoStore = ''

			//2、专业培养目标及要求：专业描述、培养目标表格
			state.subjectDescriptionStore = ''
			state.tableDataCultivationGoal = [
				{
					serial: Math.random().toString(36).slice(2),
					CultivationGoal: '培养要求',
					description: '描述'
				}
			]

			//3、毕业要求及指标点
			state.graduateRequestTable = [
				{
					info: "",
					points: [
						{
							point: '',
						},
					]
				},
			]

			//4、培养目标与毕业要求对应表
			state.GoalMatchRequest = [
				// {
				// 	requsetIdx:毕业要求1,
				// 	培养目标1:0,
				//  培养目标2:1,
				// },
			]

			//5、教学计划表
			state.tableCourseInFosterplan = [
				{
					courseCode: 'soft000',
					courseName: '课程名称',
					courseCategory: '专业基础课程',
					credits: '0',
					hours: '0',
					semester: '第一学年上',
					isRequired: '必修',
				},
			]

			//6、课程权重（课程对每个毕业指标点的贡献）
			state.CourseMatchRequest = [
				// {
				// 	courseName: '课程名称',
				// 	'1-1':0
				// },
			]

			//7、课程对毕业要求支撑关系
			state.CourseSupportRequest = [
				// {
				// 	courseName:'',
				// 	'1':'',
				// }
			]

			//8、评价机制
			state.evaluationMechanismStore = ''
		},

		//新建大纲：当前新建大纲的课程名、专业、年级更新
		updateNewClassNameStore(state, str) {
			state.newClassNameStore = str;
		},

		updateNewClassSubjectStore(state, str) {
			state.newClassSubjectStore = str;
		},

		updateNewClassYearStore(state, str) {
			state.newClassYearStore = str;
		},

		//新建大纲：当前新建大纲的课程简介更新
		updateCourseBriefInfoStore(state, str) {
			state.courseBriefInfoStore = str;
		},

		//课程大纲新建或取消后清除数据项
		clearClassPlan(state) {

			//1、课程名、专业、适用年级、课程简介
			state.newClassNameStore = ''
			state.newClassSubjectStore = ''
			state.newClassYearStore = ''
			state.courseBriefInfoStore = ''

			//2、课程章节知识点添加 3、课程章节学时分配
			state.chapterData = [
				{
					chapterName: '',
					//理论学时、实践学时、自主学习学时、说明
					theoryHours: 0,
					practiceHours: 0,
					selfLearningHours: 0,
					description: '',
					keyPoints: [
						{
							keyPoint: '',
						},
					]
				},
			]

			//4、课程目标添加:课程目标表，课程目标对毕业指标点权重表
			state.courseGoalTable = [
				{
					goal: '',
					pointIndex: [
						// '1-1',
						// '2-1'
					],
					homeworkRatio: 0,
					examRatio: 0,
					experienceRatio: 0
				},
			]

			state.courseGoalWeightTable = [
				// {
				// 	pointIndex:'',
				// 	courseGoalIndex:'',
				//  courseGoal:'',
				//  weight:''
				// },
			]
		}
	}
})