const EMOJIS = [
  "👍","❤️","🔥","🥰","👏","😁","🤔","🤯","😱","😢",
  "🎉","🤩","🙏","👌","🕊","🤡","🥱","🥴","😍","🤷‍♂️",
  "❤️‍🔥","🌚","💯","🤣","⚡","🏆","🗿","😐","🤨","🍾",
  "💋","😈","😴","😭","🤓","👻","👨‍💻","👀","🙈","🤷‍♀️",
  "😇","🤝","✍️","🤗","🫡","😨","🧑‍🎄","🎄","⛄","🤪",
  "🆒","💘","🙊","🦄","😘","🙉","💊","😎","👾","🤷"
];

export default {
  async fetch(request, env) {
    const u = await request.json();
    if (!u.message) return new Response("ok");

    const m = u.message;
    const c = m.chat.id;
    const mid = m.message_id;

    const emoji = EMOJIS[Math.floor(Math.random() * EMOJIS.length)];

    await fetch(`https://api.telegram.org/bot${env.BOT_TOKEN}/setMessageReaction`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        chat_id: c,
        message_id: mid,
        reaction: [{ type: "emoji", emoji }]
      })
    });

    return new Response("ok");
  }
};
