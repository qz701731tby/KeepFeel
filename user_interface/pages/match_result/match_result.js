// pages/match_result/match_result.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    url: "",
    openId: "",
    result:[],
    empty: 0
  },

  jump: function(e){
    wx.navigateTo({
      url: '../others/others',})
  },

  jump_to_others_space: function(e){
    var app = getApp()
    //console.log('target_wechat_id = ', target_wechat_id)
    wx.request({
      url: 'http://10.209.102.112:5001/',
      data: {
        mark: 4,
        openId: e.currentTarget.dataset.total,
      },
      header: { 'content-type': 'application/json' },
      //method: 'POST',
      success: function (res) {
        console.log(res.data)
        app.globalData.target_info = res.data
        console.log('目标信息是：' + app.globalData.target_info)
        wx.navigateTo({
          url: '../others/others',
        })
      },
      fail: function (err) {
        console.log(err)
      }
    })
    // setTimeout(function(){wx.navigateTo({
    //   url: '../others/others',
    // })}, 2000) 
  },
 
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var app = getApp()
    console.log("返回结果长度是" + app.globalData.match_result.length)
    if (app.globalData.match_result.length == 0) {
      this.setData({
        empty : 1
      })
    }
    this.setData({
      result: app.globalData.match_result,
      url: app.globalData.imgUrl
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