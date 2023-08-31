<template>
    <div class="course_goal">
        <el-button type="primary" @click="switchIndex = 1" style="margin-bottom: 20px;">编辑课程目标</el-button>
        <el-button type="primary" @click="switchIndex = 2" style="margin-bottom: 20px;">设置课程权重</el-button>
        <div class="edit_course_goal" v-if="switchIndex == 1">
            <!-- 添加课程目标 -->
            <el-button type="success" @click="addCourseGoal" style="margin-bottom: 20px;">添加课程目标</el-button>
            <div class="course_goaL_scroll_bar">
                <div class="course_goal_box" v-for="(item, index) in courseGoalTable" :key="index">
                    <!-- 课程目标关键字输入 -->
                    <div class="goal_content">
                        <span>课程目标{{ index + 1 }}:</span><br />
                        <el-input class="goal_content_input" v-model="item.goal" :rows="4" type="textarea" resize="none"
                            placeholder="简介..." />
                    </div>
                    <!-- 课程目标对应指标点选择 -->
                    <div class="point_select">
                        <span>指标点选择：</span><br /><br />
                        <el-select v-model="item.pointIndex" @change="setCourseGoalWeight" multiple placeholder="请选择指标点"
                            style="width: 240px" clearable="true" no-data-text="暂无数据">
                            <el-option v-for="item in allPoints" :key="item.pointIndex" :label="item.pointIndex"
                                :value="item.pointIndex" />
                        </el-select>
                    </div>
                    <!-- 删除课程目标 -->
                    <div class="handle_btn">
                        <br /><br />
                        <el-button type="danger" v-if="courseGoalTable.length > 1"
                            @click="removeCourseGoal(item, index)">删除</el-button>
                    </div>
                </div>
            </div>

        </div>
        <div class="set_course_weight" v-if="switchIndex == 2">
            <el-button type="success" @click="setCourseGoalWeight" style="margin-bottom: 20px;">生成权重表格</el-button>
            <div class="course_weight_scroll_bar">
                <el-table :data="this.courseGoalWeightTable" :span-method="objectSpanMethod" border fit size="mini"
                    empty-text="暂无数据" style="width:345px;">
                    <el-table-column prop="pointIndex" label="指标点" align="center" width="100px"> </el-table-column>
                    <el-table-column prop="courseGoalIndex" label="课程目标" align="center" width="100px"> </el-table-column>
                    <el-table-column prop="weight" label="权重" align="center" width="145px">
                        <template #default="scope">
                            <el-input-number size="small" controls-position="right" min="0" max="1" step="0.1"
                                value-on-clear="min" v-model="scope.row.weight"></el-input-number>
                        </template>
                    </el-table-column>
                </el-table>
            </div>

        </div>
    </div>
</template>
  
<script>
import { mapState } from 'vuex';
import { getWeight } from '../../api/api.js'

export default {
    name: 'CourseGoal',
    components: {

    },

    data() {
        return {
            allPoints: [],//当前课程相关的指标点
            switchIndex: 1,
            spanArr: [], // 一个空的数组，用于存放每一行记录的合并数
            pos: 0, // spanArr 的索引
        }
    },

    computed: {
        ...mapState(["courseGoalTable", "courseGoalWeightTable", "newClassNameStore", "newClassYearStore"]),
    },

    mounted() {
        //获取当前课程对应的所有指标点
        getWeight(this.newClassYearStore, this.newClassNameStore).then(response => {
            this.allPoints.length = 0;
            for (var i = 0; i < response.data.content.length; i++) {
                var data = response.data.content[i];
                this.allPoints.push({
                    pointIndex: data.pointIndex,
                })
            }

            //对可选指标点进行排序，便于指标点的选取
            for (var j = 0; j < this.allPoints.length - 1; j++) {
                for (i = 0; i < this.allPoints.length - 1; i++) {
                    let item1 = this.allPoints[i]
                    let item2 = this.allPoints[i + 1]
                    let count1 = Number(item1.pointIndex.charAt(0)) * 10 + Number(item1.pointIndex.charAt(2))
                    let count2 = Number(item2.pointIndex.charAt(0)) * 10 + Number(item2.pointIndex.charAt(2))
                    if (count1 > count2) {
                        this.allPoints[i] = this.allPoints.splice(i + 1, 1, this.allPoints[i])[0]
                    }
                }
            }
        })
    },

    methods: {
        //添加课程目标
        addCourseGoal() {
            // 定义一个标识，通过标识判断是否能添加信息
            let statusType = true;
            this.courseGoalTable.forEach((item) => {
                if (
                    item.goal == ""
                ) {
                    this.$message({
                        message: "请完善信息后在添加",
                        type: "warning",
                    });
                    statusType = false;
                }
            });
            if (statusType) {
                this.courseGoalTable.push({
                    goal: '',
                    pointIndex: [
                    ],
                    homeworkRatio: 0,
                    examRatio: 0,
                    experienceRatio: 0
                });
                this.setCourseGoalWeight();
            }
        },

        //删除课程目标
        removeCourseGoal(item, index) {
            this.courseGoalTable.splice(index, 1);
            this.$message({
                message: "删除成功",
                type: "success",
            });
            this.setCourseGoalWeight();
        },

        //生成权重表格
        setCourseGoalWeight() {
            //根据课程目标表生成课程目标权重数据
            this.courseGoalWeightTable.length = 0
            var goalIndex = 1
            for (let key in this.courseGoalTable) {
                for (let kkey in this.courseGoalTable[key].pointIndex) {
                    this.courseGoalWeightTable.push({
                        pointIndex: this.courseGoalTable[key].pointIndex[kkey],
                        courseGoalIndex: goalIndex,
                        courseGoal: this.courseGoalTable[key].goal,
                        weight: ''
                    })
                }
                goalIndex += 1
            }

            //对课程目标权重数据进行排序
            for (var j = 0; j < this.courseGoalWeightTable.length - 1; j++) {
                for (var i = 0; i < this.courseGoalWeightTable.length - 1; i++) {
                    let item1 = this.courseGoalWeightTable[i]
                    let item2 = this.courseGoalWeightTable[i + 1]
                    let count1 = Number(item1.pointIndex.charAt(0)) * 10 + Number(item1.pointIndex.charAt(2))
                    let count2 = Number(item2.pointIndex.charAt(0)) * 10 + Number(item2.pointIndex.charAt(2))
                    if (count1 > count2) {
                        this.courseGoalWeightTable[i] = this.courseGoalWeightTable.splice(i + 1, 1, this.courseGoalWeightTable[i])[0]
                    }
                }
            }

            this.getList();
        },

        // eslint-disable-next-line
        objectSpanMethod({ row, column, rowIndex, columnIndex }) {
            if (columnIndex === 0) {
                const _row = this.spanArr[rowIndex];
                const _col = _row > 0 ? 1 : 0;
                return {
                    rowspan: _row,
                    colspan: _col
                };
            }
        },

        // 获取列表数据
        getList() {
            // 设定一个数组spanArr/contentSpanArr来存放要合并的格数，同时还要设定一个变量pos/position来记录
            this.spanArr = [];
            for (var i = 0; i < this.courseGoalWeightTable.length; i++) {
                if (i === 0) {
                    this.spanArr.push(1);
                    this.pos = 0;
                } else {
                    // 判断当前元素与上一个元素是否相同(第1和第2列)
                    if (this.courseGoalWeightTable[i].pointIndex === this.courseGoalWeightTable[i - 1].pointIndex) {
                        this.spanArr[this.pos] += 1;
                        this.spanArr.push(0);
                    } else {
                        this.spanArr.push(1);
                        this.pos = i;
                    }
                }
            }
        },
    }
}
</script>
  
<style>
.goal_content {
    float: left;
    width: 40%;
    margin-bottom: 20px;
}

.point_select {
    float: left;
    width: 20%;
    height: 140px;
    margin-bottom: 20px;
}

.handle_btn {
    float: left;
    height: 160px;
    width: 40%;
}

.goal_content_input {
    margin-top: 20px;
    width: 500px !important;
}

.course_goaL_scroll_bar {
    width: 1300px;
    height: 650px;
    overflow-y: auto;
}

.course_goaL_scroll_bar::-webkit-scrollbar {
    width: 8px;
}

.course_goaL_scroll_bar::-webkit-scrollbar-thumb {
    background-color: #ccc;
}

.course_goaL_scroll_bar::-webkit-scrollbar-thumb:hover {
    background-color: #aaa;
}

.course_weight_scroll_bar {
    width: 355px;
    height: 650px;
    overflow-y: auto;
}

.course_weight_scroll_bar::-webkit-scrollbar {
    width: 8px;
}

.course_weight_scroll_bar::-webkit-scrollbar-thumb {
    background-color: #ccc;
}

.course_weight_scroll_bar::-webkit-scrollbar-thumb:hover {
    background-color: #aaa;
}
</style>