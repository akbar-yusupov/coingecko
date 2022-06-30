const { createApp } = Vue;

const CoinsApp = {
  data(){
    return {
      coin: "Just a coin",
      coins: null
    }
  },
  created(){
    const socket = new WebSocket(`ws://${window.location.host}/ws/cryptocurrencies`);

    let _this = this;

    socket.onmessage = function(event){
      _this.coins = JSON.parse(event['data']);
    }
  }
}

createApp(CoinsApp).mount("#app")

