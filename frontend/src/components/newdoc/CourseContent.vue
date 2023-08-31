<template>
    <div class="course_content">
        <div class="formOuterBox" v-for="(item, index) in chapterData" :key="index">
            <div class="formCotantBox">
                <h4>第{{ index + 1 }}章</h4>
                <!-- 章节表单内容 -->
                <!-- eslint-disable-next-line -->
                <el-form label-width="80px" @submit.native.prevent>
                    <!-- 章节名称填写 -->
                    <el-form-item label="章节名称">
                        <el-input v-model="item.chapterName"></el-input>
                    </el-form-item>
                    <!-- 知识点表格 -->
                    <el-table :data="item.keyPoints" :index="indexMethod" stripe border>
                        <el-table-column type="index" label="序号" width="80px" />
                        <el-table-column prop="keyPoint" label="知识点" width="400px" :show-overflow-tooltip="true" />
                        <el-table-column prop="" label="操作" width="120px">
                            <template #default="scope">
                                <button class="goal_btn"
                                    @click="editKeyPoint(index, scope.row, scope); KeyPointDialogVisible = true">编辑</button>
                                <button class="goal_btn" style="margin-left:5px" v-if="item.keyPoints.length > 1"
                                    @click="deleteKeyPoint(item, scope)">删除</button>
                            </template>
                        </el-table-column>
                    </el-table>
                    <!-- 添加知识点 -->
                    <button class="add_graduate_point_btn" @click="addKeyPoint(item)">添加</button>
                </el-form>
                <!-- 编辑知识点 -->
                <el-dialog v-model="KeyPointDialogVisible" title="本章知识点">
                    <el-form ref="form" :model="currentKeyPoint">
                        <el-form-item label="知识点">
                            <el-input v-model="currentKeyPoint.keyPoint"></el-input>
                        </el-form-item>
                    </el-form>
                    <div>
                        <el-button @click="KeyPointDialogVisible = false">取消</el-button>
                        <el-button type="primary" @click="saveKeyPoint()">保存</el-button>
                    </div>
                </el-dialog>

            </div>
            <!-- 添加毕业要求 -->
            <div>
                <el-button v-if="index == chapterData.length - 1" @click="addChapter" type="success">添加章节</el-button>
                <el-button v-if="chapterData.length > 1" @click="removeIdx(item, index)" type="danger">删除此章节</el-button>
            </div>
        </div>
    </div>
</template>
  
<script>
import { mapState } from 'vuex';

export default {
    name: 'CourseContent',
    components: {

    },

    data() {
        return {
            KeyPointDialogVisible: false,//控制知识点编辑表单显示
            currentKeyPoint: {},//当前编辑知识点
            currentIdx: -1,//当前编辑知识点下标
            currentChapterIdx: -1,//当前编辑章节下标
        }
    },

    computed: {
        ...mapState(["chapterData"]),
    },

    methods: {
        addChapter() {
            // 定义一个标识，通过标识判断是否能添加信息
            let statusType = true;
            this.chapterData.forEach((item) => {
                if (
                    item.chapterName == ""
                ) {
                    this.$message({
                        message: "请补充当前章节名称后添加新章节",
                        type: "warning",
                    });
                    statusType = false;
                }
            });
            if (statusType) {
                this.chapterData.push({
                    chapterName: "",
                    theoryHours: 0,
                    practiceHours: 0,
                    selfLearningHours: 0,
                    description: '',
                    keyPoints: [
                        {
                            keyPoint: '',
                        },
                    ]
                });
            }
        },

        // 删除操作
        removeIdx(item, index) {
            this.chapterData.splice(index, 1);
            this.$message({
                message: "删除成功",
                type: "success",
            });
        },

        //添加毕业指标点
        addKeyPoint(item) {
            item.keyPoints.push({
                keyPoint: '',
            },)
        },

        //删除毕业指标点
        deleteKeyPoint(item, scope) {
            item.keyPoints.splice(scope.$index, 1);
        },

        //编辑毕业指标点
        editKeyPoint(index, row, scope) {
            this.currentKeyPoint = Object.assign({}, row);
            this.currentIdx = scope.$index;
            this.currentChapterIdx = index;
        },

        //保存编辑内容
        saveKeyPoint() {
            Object.assign(this.chapterData[this.currentChapterIdx].keyPoints[this.currentIdx], this.currentKeyPoint);
            this.KeyPointDialogVisible = false;
        },

        //毕业指标点index生成
        indexMethod(index) {
            return index + 1;
        }
    }
}
</script>
  
<style>
.course_content {
    width: 700px;
    height: 650px;
    overflow-y: auto;
}

.course_content::-webkit-scrollbar {
    width: 8px;
}

.course_content::-webkit-scrollbar-thumb {
    background-color: #ccc;
}

.course_content::-webkit-scrollbar-thumb:hover {
    background-color: #aaa;
}
</style>