// pages/me/me.js
//获取应用实例
var app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    //用户个人信息
    avatar: "https://img1.baidu.com/it/u=4206129941,2422852433&fm=26&fmt=auto",//用户头像
    nickname: "",//用户昵称
    gender:0,//用户性别
    wechatId:"",//用户的微信号
    intro:"",//个人介绍
    // openid : "",//用户openid
    imgUrl:"",
    photo: ['/image/ImgWallEmpty.jpg']
    // photo: ""
  },
  /**
   *点击添加地址事件
   */
  add_address_fun: function () {
    wx.navigateTo({
      url: 'add_address/add_address',
    })
  },

  // ImgChoose: function () {
  //   var that = this
  //   wx.chooseImage({
  //     count: 3,
  //     success: function (res) {
  //       console.log(res)
  //       that.setData({
  //         imageList: res.tempFilePaths
  //       })
  //     }
  //   })
  // },

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
  // onLoad: function (options) {
  //   console.log("加载了")
  //   var app = getApp()
  //   // var nn = app.globalData.userInfo.avatar
  //   // console.log(nn)
  //   /**
  //    * 获取用户信息
  //    */
  //   // console.log(this.data.photo)
  //   this.setData({
  //     wechatId: app.globalData.userInfo.wechatId,
  //     nickname: app.globalData.userInfo.nickname,
  //     avatar: app.globalData.imgUrl + app.globalData.userInfo.avatar,
  //     gender:app.globalData.userInfo.gender,
  //     intro: app.globalData.userInfo.intro,
  //     // photo: [app.globalData.imgUrl + app.globalData.userInfo.photo],
  //   })
  //   // console.log(this.data.photo)
  //   // wx.getUserInfo({
  //   //   success: function (res) {
  //   //     console.log(res);
  //   //     var avatarUrl = 'userInfo.avatarUrl';
  //   //     var nickName = 'userInfo.nickName';
  //   //     var gender='userInfo.gender';
  //   //     var city='userInfo.city';
  //   //     that.setData({
  //   //       [avatarUrl]: res.userInfo.avatarUrl,
  //   //       [nickName]: res.userInfo.nickName,
  //   //       [gender]:res.userInfo.gender,
  //   //       [city]:res.userInfo.city,
  //   //     })
  //   //   }
  //   // })
  // },

  refresh_info: function(){
    wx.navigateTo({
      url: '../refresh/refresh',
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
    console.log("显示了")
    var app = getApp()
    console.log("微信ID是：" + app.globalData.userInfo.intro)
    // var nn = app.globalData.userInfo.avatar
    // console.log(nn)
    /**
     * 获取用户信息
     */
    this.setData({
      wechatId: app.globalData.userInfo.wechatId,
      nickname: app.globalData.userInfo.nickname,
      avatar: app.globalData.imgUrl + app.globalData.userInfo.avatar.slice(1),
      gender:app.globalData.userInfo.gender,
      intro: app.globalData.userInfo.intro,
      imgUrl: app.globalData.imgUrl,
      photo: [app.globalData.userInfo.photo.slice(1)],
    })
    console.log(this.data.avatar)
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
