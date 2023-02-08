// Basic Offline mode random string bot script

const mineflayer = require("mineflayer");

// Generate random string
function makeid(length) {
    let result = '';
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    const charactersLength = characters.length;
    let counter = 0;
    while (counter < length) {
      result += characters.charAt(Math.floor(Math.random() * charactersLength));
      counter += 1;
    }
    return result;
}
// Choose usernames and IP
console.log(makeid(5));
var settings = {
    username: (makeid(5)),
    host: "bruhland.apexmc.co",
};
// Bot actions upon joining

const bot = mineflayer.createBot(settings);
bot.once("spawn", ()=>{
    bot.chat(makeid(20));
  });

