export const getUsers = async () => {
  const res = await fetch(`${process.env.BASE_URL}/api/users`);
  const data = res.json();
  return data;
};
