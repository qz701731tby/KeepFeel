// pages/me/me.js
//获取应用实例
var app = getApp
Page({

  /**
   * 页面的初始数据
   */
  data: {
    //用户个人信息
    avatarUrl: '',
    target_user_info: {},
    photo: ['/image/RMCF.jpg',
      '/image/CR7.jpg',
      '/image/Luka.jpg'],
      imgUrl:''
  },

  ImgPreview: function (e) {
    var current = e.target.dataset.src
    wx.previewImage({
      current: current,
      urls: this.data.imageList
    })
  },
  
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function () {
    var app = getApp()
    this.setData({
      target_user_info: app.globalData.target_info,
      avatarUrl: app.globalData.imgUrl + app.globalData.target_info.avatar.slice(1),
      photo: [app.globalData.imgUrl + app.globalData.target_info.photo.slice(1)],
      imgUrl: app.globalData.imgUrl
    })
    console.log(this.data.avatarUrl)
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
    // this.setData({
    //   target_user_info: getApp().globalData.target_info
    // })
    // console.log(this.data.target_info)
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
