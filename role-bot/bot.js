const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', msg => {
  if (msg.content === '!hi') {
    msg.reply('Hello!');
  }
});
/*
client.on('guildMemberAdd', member => {
  const channel = member.guild.channels.find('name', 'member-log');
  if (!channel) return;
  channel.send(`Welcome to the server, ${member}`);
});
*/

client.login('NDQ1NDUxNDk2OTU2NjI0ODk4.DdvM5Q.mN7i4ZaOzqU2eY-5BmjKg-5X6q0');