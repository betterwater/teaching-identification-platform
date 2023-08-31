import axiosInstance from './index'

const axios = axiosInstance

// export const getBooks = () => {return axios.get(`http://localhost:8000/api/books/`)}

// export const postBook = (bookName, bookAuthor) => {return axios.post(`http://localhost:8000/api/books/`, {'name': bookName, 'author': bookAuthor})}

export const login = (userAccount, userPassword) => { return axios.post(`http://127.0.0.1:8000/api/users/login/`, { 'userAccount': userAccount, 'userPassword': userPassword }) }


//------------------------------------------------------------------------------------------------------fosterplan
//无 / facility、year、subject
export const getAll = () => { return axios.post(`http://127.0.0.1:8000/api/fosterPlan/getAll/`) }

//facility、year、subject、briefInfo、subjectDescription、evaluationMechanism / 无
export const uploadPlan = (facility, year, subject, briefInfo, subjectDescription, evaluationMechanism) => { return axios.post(`http://127.0.0.1:8000/api/fosterPlan/uploadPlan/`, { 'facility': facility, 'year': year, 'subject': subject, 'briefInfo': briefInfo, 'subjectDescription': subjectDescription, 'evaluationMechanism': evaluationMechanism }) }


//------------------------------------------------------------------------------------------------------CultivationGoal
//facility、year、subject、index、cultivationGoal、description / 无
export const uploadCG = (facility, year, subject, index, cultivationGoal, description) => { return axios.post(`http://127.0.0.1:8000/api/cultivationGoal/uploadCG/`, { 'facility': facility, 'year': year, 'subject': subject, 'index': index, 'cultivationGoal': cultivationGoal, 'description': description }) }


//------------------------------------------------------------------------------------------------------GraduateRequest
//facility、subject、year / requestIndex、graduateRequest、pointIndex、indexPoint
export const getRequest = (facility, year, subject) => { return axios.post(`http://127.0.0.1:8000/api/graduateRequest/getRequest/`, { 'facility': facility, 'year': year, 'subject': subject }) }

//facility、year、subject、requestIndex、graduateRequest、pointIndex、indexPoint / 无
export const uploadRequest = (facility, year, subject, requestIndex, graduateRequest, pointIndex, indexPoint) => { return axios.post(`http://127.0.0.1:8000/api/graduateRequest/uploadRequest/`, { 'facility': facility, 'year': year, 'subject': subject, 'requestIndex': requestIndex, 'graduateRequest': graduateRequest, 'pointIndex': pointIndex, 'indexPoint': indexPoint }) }


//------------------------------------------------------------------------------------------------------GoalAndRequest
//facility、year、subject、index、requestIndex / 无
export const uploadGR = (facility, year, subject, index, requestIndex) => { return axios.post(`http://127.0.0.1:8000/api/goalAndRequest/uploadGR/`, { 'facility': facility, 'year': year, 'subject': subject, 'index': index, 'requestIndex': requestIndex }) }


//------------------------------------------------------------------------------------------------------CourseInFosterPlan
//facility、year、subject、className、courseCategory、credits、hours、semester、isRequired / 无
export const uploadCIFP = (facility, year, subject, className, courseCategory, credits, hours, semester, isRequired) => { return axios.post(`http://127.0.0.1:8000/api/courseInFosterPlan/uploadCIFP/`, { 'facility': facility, 'year': year, 'subject': subject, 'className': className, 'courseCategory': courseCategory, 'credits': credits, 'hours': hours, 'semester': semester, 'isRequired': isRequired }) }

//subject、className、year / courseCategory、credits、hours、semester、isRequired
export const getCourse = (subject, className, year) => { return axios.post(`http://127.0.0.1:8000/api/courseInFosterPlan/getCourse/`, { 'subject': subject, 'className': className, 'year': year }) }


//------------------------------------------------------------------------------------------------------CourseWeight
//year、className / pointIndex、weight
export const getWeight = (year, className) => { return axios.post(`http://127.0.0.1:8000/api/courseWeight/getWeight/`, { 'year': year, 'className': className }) }

//facility、subject、year / pointIndex、className、weight
export const getPointW = (facility, year, subject) => { return axios.post(`http://127.0.0.1:8000/api/courseWeight/getPointW/`, { 'facility': facility, 'year': year, 'subject': subject }) }

//facility、year、subject、pointIndex、className、weight / 无
export const uploadCW = (facility, year, subject, pointIndex, className, weight) => { return axios.post(`http://127.0.0.1:8000/api/courseWeight/uploadCW/`, { 'facility': facility, 'year': year, 'subject': subject, 'pointIndex': pointIndex, 'className': className, 'weight': weight }) }


//------------------------------------------------------------------------------------------------------ClassSupportRequest
//facility、year、subject、className、requestIndex、weight / 无
export const uploadCSR = (facility, year, subject, className, requestIndex, weight) => { return axios.post(`http://127.0.0.1:8000/api/classSupportRequest/uploadCSR/`, { 'facility': facility, 'year': year, 'subject': subject, 'className': className, 'requestIndex': requestIndex, 'weight': weight }) }


//------------------------------------------------------------------------------------------------------ClassPlan
//无 / className、year、userAccount | | userAccount / username
export const getAllPlan = () => { return axios.post(`http://127.0.0.1:8000/api/classPlan/getAllPlan/`) }

//userAccount / className、year
export const getMine = (userAccount) => { return axios.post(`http://127.0.0.1:8000/api/classPlan/getMine/`, { 'userAccount': userAccount }) }

//userAccount、className、year 、classInfo/ 无
export const uploadClass = (userAccount, className, year, classInfo) => { return axios.post(`http://127.0.0.1:8000/api/classPlan/uploadClass/`, { 'userAccount': userAccount, 'className': className, 'year': year, 'classInfo': classInfo }) }

//className、year / 无
export const deleteCP = (className, year) => { return axios.post(`http://127.0.0.1:8000/api/classPlan/deleteCP/`, { 'className': className, 'year': year }) }


//------------------------------------------------------------------------------------------------------ClassContent
//className、year、chapterIndex、chapter、keyPointIndex、keyPoint / 无
export const uploadCC = (className, year, chapterIndex, chapter, keyPointIndex, keyPoint) => { return axios.post(`http://127.0.0.1:8000/api/classContent/uploadCC/`, { 'className': className, 'year': year, 'chapterIndex': chapterIndex, 'chapter': chapter, 'keyPointIndex': keyPointIndex, 'keyPoint': keyPoint }) }

//className、year / 无
export const deleteCContent = (className, year) => { return axios.post(`http://127.0.0.1:8000/api/classContent/deleteCContent/`, { 'className': className, 'year': year }) }


//------------------------------------------------------------------------------------------------------ClassHours
//className、year、chapterIndex、theoryHours、practiceHours、selfLearningHours、description / 无
export const uploadCH = (className, year, chapterIndex, theoryHours, practiceHours, selfLearningHours, description) => { return axios.post(`http://127.0.0.1:8000/api/classHours/uploadCH/`, { 'className': className, 'year': year, 'chapterIndex': chapterIndex, 'theoryHours': theoryHours, 'practiceHours': practiceHours, 'selfLearningHours': selfLearningHours, 'description': description }) }

//className、year / 无
export const deleteCH = (className, year) => { return axios.post(`http://127.0.0.1:8000/api/classHours/deleteCH/`, { 'className': className, 'year': year }) }


//------------------------------------------------------------------------------------------------------ClassData
//className、year、data（homework、exp、exam） / 无
export const uploadData = (className, year, homework, experience, exam) => { return axios.post(`http://127.0.0.1:8000/api/classData/uploadData/`, { 'className': className, 'year': year, 'homework': homework, 'experience': experience, 'exam': exam }) }

//className、year / homework、exam、experience
export const getData = (className, year) => { return axios.post(`http://127.0.0.1:8000/api/classData/getData/`, { 'className': className, 'year': year }) }

//className、year / 无
export const deleteCData = (className, year) => { return axios.post(`http://127.0.0.1:8000/api/classData/deleteCData/`, { 'className': className, 'year': year }) }


//------------------------------------------------------------------------------------------------------ClassDataRatio
//year、className / classTarget、homeworkRatio、examRatio、experienceRatio、courseGoalAttainment
export const getRatio = (year, className) => { return axios.post(`http://127.0.0.1:8000/api/classDataRatio/getRatio/`, { 'year': year, 'className': className }) }

//className、year、classTargetIndex、homeworkRatio、examRatio、experienceRatio / 无
export const uploadRatio = (className, year, classTargetIndex, homeworkRatio, examRatio, experienceRatio) => { return axios.post(`http://127.0.0.1:8000/api/classDataRatio/uploadRatio/`, { 'className': className, 'year': year, 'classTargetIndex': classTargetIndex, 'homeworkRatio': homeworkRatio, 'examRatio': examRatio, 'experienceRatio': experienceRatio }) }

//className、year / 无
export const deleteCDR = (className, year) => { return axios.post(`http://127.0.0.1:8000/api/classDataRatio/deleteCDR/`, { 'className': className, 'year': year }) }


//------------------------------------------------------------------------------------------------------IndexPointContent
//year、className / indexPoint、classTargetIndex、classTarget、weight
export const getTarget = (year, className) => { return axios.post(`http://127.0.0.1:8000/api/indexPointContent/getTarget/`, { 'year': year, 'className': className }) }

//className、year、classTargetIndex、classTarget、pointIndex、weight / 无
export const uploadIPC = (className, year, classTargetIndex, classTarget, pointIndex, weight) => { return axios.post(`http://127.0.0.1:8000/api/indexPointContent/uploadIPC/`, { 'className': className, 'year': year, 'classTargetIndex': classTargetIndex, 'classTarget': classTarget, 'pointIndex': pointIndex, 'weight': weight }) }

//className、year / 无
export const deleteIPC = (className, year) => { return axios.post(`http://127.0.0.1:8000/api/indexPointContent/deleteIPC/`, { 'className': className, 'year': year }) }


//------------------------------------------------------------------------------------------------------IndexPointResult
//year、className、pointIndex 、goal / 无
export const uploadGoal = (year, className, pointIndex, goal) => {return axios.post(`http://127.0.0.1:8000/api/indexPointResult/uploadGoal/`, {'year': year, 'className': className, 'pointIndex': pointIndex, 'goal': goal})}

//year、className、pointIndex / goal
export const getPoint = (year, className, pointIndex) => {return axios.post(`http://127.0.0.1:8000/api/indexPointResult/getPoint/`, {'year': year, 'className': className, 'pointIndex': pointIndex})}

//className、year / 无
export const deleteIPR = (year, className) => {return axios.post(`http://127.0.0.1:8000/api/indexPointResult/deleteIPR/`, {'year': year, 'className': className })}
