// MICROSOFT AUTH SIMPLE BOT TEMPLATE
// VARIABLES

var alt = ['alt1@gmail.com', 'alt2@gmail.com']
var pass = ['pass1', 'pass2'] 

const mineflayer = require('mineflayer')
const bot = mineflayer.createBot({

  // SERVER
  host: 'bruhland.apexmc.co',
  port: 25565,
  
  // MS AUTH 
  username: 'Mymail@gmail.com', // alt[0] alt[1] etc
  password: 'Pass', // pass
  auth: 'microsoft'
	});
	
  // Bot actions upon joining

	bot.once("spawn", ()=>{
    bot.chat("TEST COMPLETE");
  });

// By Silverainox
