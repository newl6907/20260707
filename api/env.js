module.exports = function handler(req, res) {
  const env = {
    SUPABASE_URL: process.env.SUPABASE_URL || '',
    SUPABASE_ANON_KEY: process.env.SUPABASE_ANON_KEY || '',
    SUPABASE_TABLE_NAME: process.env.SUPABASE_TABLE_NAME || 'lotto_draws',
  };

  res.setHeader('Content-Type', 'application/javascript; charset=utf-8');
  res.setHeader('Cache-Control', 'no-store');
  res.status(200).send(`window.__ENV__ = ${JSON.stringify(env)};`);
};
