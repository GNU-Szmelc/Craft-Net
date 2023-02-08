// Basic web viewer prismarine script
// 
const mineflayer = require('mineflayer')
const inventoryViewer = require('mineflayer-web-inventory')
const { mineflayer: mineflayerViewer } = require('prismarine-viewer')

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
//var host = ["1b1t.org"]

const bot = mineflayer.createBot({
  // SERVER SELECTOR API
  host: 'bruhland.apexmc.co',
  //port: 25565,
  // AUTH API
  username: makeid(5),
  //auth: 'microsoft'
});

// Bot actions upon joining
// VIEWER
	bot.once('spawn', () => {
  mineflayerViewer(bot, { port: 3007, firstPerson: false })
  });


