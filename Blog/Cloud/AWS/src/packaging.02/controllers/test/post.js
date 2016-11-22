module.exports = (userId, header, body) => {
  return {
    body: { id: userId, header: header, body: body }
  };
};