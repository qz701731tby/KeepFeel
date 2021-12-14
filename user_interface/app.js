App(
  {
    globalData: {
      // openid: null,
      userInfo: null,
      match_result: null,
      target_info: {},
      serverUrl:'http://10.209.102.112:5001/',
      imgUrl:'http://10.209.102.112:8080'
    },
    onLaunch: function () {
      var that = this
      wx.login({
        success: function(res) {
          var code = res.code; //返回code
          console.log(code);
          if (res.code) {
            //发起网络请求
            wx.request({
              url: that.globalData.serverUrl,
              data: {
                mark: 0,
                code: res.code
              },
              method: 'get',
              success: function (res) {
                console.log(res.data)
                that.globalData.userInfo = res.data
              },
              fail: function (err) {
                console.log(err)
              }
            })
          } else {
            console.log('获取用户登录态失败！' + res.errMsg)
          }
        },
      });
    
    // getUserInfo: function (cb) {
    //   var that = this
    //   wx.login({
    //     success: function () {
    //       wx.getUserInfo({
    //         success: function (res) {
    //           that.globalData.userInfo = res.userInfo
    //           typeof cb == "function" && cb(that.globalData.userInfo)
    //         }
    //       })
    //     }
    //   })
    // },
  }
})
