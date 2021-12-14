// pages/ground/ground.js
const app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    motto: '搜索',
    resultnumber: '共计' + 10 + '个结果',
    keyword:'',
    location_data: [],
    user_latitude: "",
    user_longitude: "",
    SportsLocation: '',
    match_result: []
  },

  bindKeyInput(e) {
    //console.log('input携带值为', e.detail.value)
    this.setData({
      keyword: e.detail.value
    })
  },

  search_location:function(e){
    console.log(this.data.user_latitude)
    console.log(this.data.user_longitude)
    var app = getApp()
    var that = this
    wx.request({
      url: 'http://10.209.102.112:5001/',
      data: {
        mark: 2,
        openId : app.globalData.userInfo.openId,
        // user_latitude: this.data.user_latitude,
        // user_longitude: this.data.user_longitude,
        // keyword:this.data.keyword,
        user_latitude: 31.22249,
        user_longitude: 121.5447,
        keyword:this.data.keyword,
        //用户当前经纬度
      },
      header: { 'content-type': 'application/json' },
      method: 'get',
      success: function (res) {
        console.log(res.data)
        that.setData({
          location_data: res.data
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
    wx.getLocation({
      type: "wgs84",
      success: (res) => {
        console.log(res)
        var latitude = res.latitude
        var longitude = res.longitude
        this.setData({
          user_latitude: latitude,
          user_longitude: longitude
        })
      },
      fail: function (err) {
        console.log(err)
      }
    })
  },

  BindLocationChange(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      SportsLocation: e.detail.value
    })
  },

  /**
   * 点击地址跳转函数
   */
  BindTap: function(e){
    var app = getApp()
    // console.log('当前场地是' + e.currentTarget.dataset.total)
    // this.setData({
    //   SportsLocation: e.currentTarget.dataset.total
    // })
    // var that = this
    // console.log('发送场地是' + this.SportsLocation)
    wx.request({
      url: 'http://10.209.102.112:5001/',
      data: {
        mark: 3,
        openId : app.globalData.userInfo.openId,
        user_latitude: 31.22249,
        SportsLocation: e.currentTarget.dataset.total
      },
      header: { 'content-type': 'application/json' },
      success: function (res) {
        console.log(res.data)
        for(var i = 0; i < res.data.length; i++){
          res.data[i].avatar = app.globalData.imgUrl + res.data[i].avatar.slice(1)
        }
        getApp().globalData.match_result = res.data
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