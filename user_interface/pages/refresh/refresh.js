// pages/me/me.js
//获取应用实例
var app = getApp();
Page({

  /**
   * 页面的初始数据
   */
  data: {
    //用户个人信息
    openId:"",
    avatar: "",//用户头像
    nickname: "",//用户昵称
    gender:0,//用户性别
    genderlist: ['隐藏', '男', '女'],
    wechatId:"",//用户的微信号
    intro:"",//个人介绍
    // openid : "",//用户openid
    photo: '',
  },
  /**
   *点击添加地址事件
   */
  add_address_fun: function () {
    wx.navigateTo({
      url: 'add_address/add_address',
    })
  },

  Avatar: function() {
    var that = this
    wx.chooseImage({
      count: 1,
      success: res => {
        that.setData({
          avatarlist : res.tempFilePaths
        })
        let imgbase64 = wx.getFileSystemManager().readFileSync(res.tempFilePaths[0], "base64")
        console.log("imgbase64是" + imgbase64)
        that.setData({
          avatar : imgbase64
        })
        // that.data.avatar = imgbase64
        // this.setData(this.data)
      }
    })
  },

  ImgChoose: function () {
    var that = this
    wx.chooseImage({
      count: 3,
      success: function (res) {
        console.log(res)
        that.setData({
          imageList: res.tempFilePaths
        })
        let imgbase64 = wx.getFileSystemManager().readFileSync(res.tempFilePaths[0], "base64")
        console.log("imgbase64是" + imgbase64)
        that.setData({
          photo : imgbase64
        })
      }
    })
  },

  inputn: function(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      nickname: e.detail.value
    })
  },

  inputw: function(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      wechatId: e.detail.value
    })
  },

  inputi: function(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      intro: e.detail.value
    })
  },

  Bindgenderchange: function(e) {
    console.log('picker发送选择改变，携带值为', e.detail.value)
    this.setData({
      gender : e.detail.value
    })
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
  onLoad: function (options) {
    // var that = this;
    // /**
    //  * 获取用户信息
    //  */
    // wx.getUserInfo({
    //   success: function (res) {
    //     console.log(res);
    //     var avatarUrl = 'userInfo.avatarUrl';
    //     var nickName = 'userInfo.nickName';
    //     var gender='userInfo.gender';
    //     var city='userInfo.city';
    //     that.setData({
    //       [avatarUrl]: res.userInfo.avatarUrl,
    //       [nickName]: res.userInfo.nickName,
    //       [gender]:res.userInfo.gender,
    //       [city]:res.userInfo.city,
    //     })
    //   }
    // })
    // app.globalData.userInfo.openId = this.data.openId
  },

  refresh_info: function(res){
    var that = this
    var app = getApp()
    console.log("openID是:" + app.globalData.userInfo.openId)
    wx.request({
      url: app.globalData.serverUrl,
      data: {
        mark: 1,
        openId: app.globalData.userInfo.openId,
        avatar: this.data.avatar,
        nickname: this.data.nickname,//用户昵称
        gender: this.data.gender,//用户性别
        wechatId: this.data.wechatId,
        intro: this.data.intro,
        photo: this.data.photo
      },
      header: { 'content-type': 'application/json' },
      // method: 'POST',
      success: function (res) {
        console.log(res)
        app.globalData.userInfo = res.data
        console.log("全局变量是：" + app.globalData.userInfo.wechatId)
        wx.switchTab({
          url: '../me/me',
        })
      },
      fail: function (err) {
        console.log(err)
      }
    })
    // app.globalData.userInfo.nickname = this.data.nickname
    // app.globalData.userInfo.avatar = this.data.avatar
    // app.globalData.userInfo.gender = this.data.gender
    // app.globalData.userInfo.wechatId = this.data.wechatId
    // app.globalData.userInfo.intro = this.data.intro
    // app.globalData.userInfo.photo = this.data.photo
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
