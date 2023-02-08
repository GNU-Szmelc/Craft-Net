// BASIC .JS RNG SPAMMER SCRIPT

const mineflayer = require("mineflayer");
const sleep = (waitTimeInMs) => new Promise(resolve => setTimeout(resolve, waitTimeInMs));

// Generate random string usernames
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
	setTimeout(() => {  bot.chat(makeid(20)); }, 1000),
	setTimeout(() => {  bot.chat(makeid(20)); }, 2000),
	setTimeout(() => {  bot.chat(makeid(20)); }, 3000);
});
