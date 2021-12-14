// pages/home/home.js
var util = require('../../utils/util.js');
Page({
  /**
   * 页面的初始数据
   */
  data: {
    openId:"",
    SportsType: ['跑步', '足球', '篮球', '排球', '乒乓球', '羽毛球', '游泳', '健身'],
    SportsLocation: [],
    index1: 0, 
    index2: 0,
    StartTime: '00:00',
    EndTime: '00:00',
    user_latitude: "",
    user_longitude: "",
    keyword:'',
    today:'',
    endday:'',
    Date:''
  },

  BindTypeChange(e) {
    var app = getApp()
    console.log('picker发送选择改变，携带值为',e.detail.value)
    this.setData({
      index1: e.detail.value
    })
    var that = this
    that.data.SportsLocation = []
    wx.request({
      url: 'http://10.209.102.112:5001/',
      data: {
        mark: 2,
        // user_latitude: this.data.user_latitude,
        // user_longitude: this.data.user_longitude,
        // keyword:this.data.keyword,
        openId: app.globalData.userInfo.openId,
        user_latitude: 31.22249,
        user_longitude: 121.5447,
        keyword: this.data.SportsType[this.data.index1],
        //用户当前经纬度
      },
      header: { 'content-type': 'application/json' },
      method: 'get',
      success: function (res) {
        console.log(res.data)
        // that.data.SportsLocation.push(res.data[1].name)
        
        for(var i = 0; i < res.data.length; i++){
          that.data.SportsLocation.push(res.data[i].name)
        }
        console.log(that.data.SportsLocation)
        that.setData({
          SportsLocation: that.data.SportsLocation
        })
        
      },
      fail: function (err) {
        console.log(err)
      }
    })
  },

  // search_location:function(e){
  //   console.log(this.data.user_latitude)
  //   console.log(this.data.user_longitude)
  //   var that = this
  //   wx.request({
  //     url: 'http://10.209.102.112:5001/',
  //     data: {
  //       mark: 2,
  //       // user_latitude: this.data.user_latitude,
  //       // user_longitude: this.data.user_longitude,
  //       // keyword:this.data.keyword,
  //       user_latitude: 31.22249,
  //       user_longitude: 121.5447,
  //       keyword: this.data.SportsType[this.data.index1],
  //       //用户当前经纬度
  //     },
  //     header: { 'content-type': 'application/json' },
  //     method: 'get',
  //     success: function (res) {
  //       console.log(res.data)
  //       for(i = 0; i < res.data.length; i++){
  //         SportsLocation.push(res.data[i].name)
  //       }
  //       // that.setData({
  //       //   SportsLocation: res.data
  //       // })
  //     },
  //     fail: function (err) {
  //       console.log(err)
  //     }
  //   })
  // },
  
  BindLocationChange(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      index2: e.detail.value
    })
  },

  BindDateChange(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      Date: e.detail.value
    })
  },

  BindStartTimeChange(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      StartTime: e.detail.value
    })
  },

  BindEndTimeChange(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      EndTime: e.detail.value
    })
  },

  BindTap(e) {
    var app = getApp()
    // console.log(this.data.StartTime)
    wx.request({
      url: 'http://10.209.102.112:5001/',
      data: {
        mark: 5,
        openId: app.globalData.userInfo.openId,
        SportsType: this.data.SportsType[this.data.index1],
        SportsLocation: this.data.SportsLocation[this.data.index2],
        date: this.data.Date,
        startTime: this.data.StartTime,
        endTime: this.data.EndTime,
        // endTime: '',
      },
      header: { 'content-type': 'application/json' },
      success: function (res) {
        console.log(res.data)
        for(var i = 0; i < res.data.length; i++){
          res.data[i].avatar = app.globalData.imgUrl + res.data[i].avatar.slice(1)
        }
        app.globalData.match_result = res.data
        wx.navigateTo({
          url: '../match_result/match_result',
        })
      },
      fail: function (err) {
        console.log(err)
      }
    })
    
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var time1 = util.formatTime(new Date());
    console.log(time1)
    var time2 = util.endTime(new Date());
    console.log(time2)
    this.setData({
      today : time1,
      endday : time2
    })
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})