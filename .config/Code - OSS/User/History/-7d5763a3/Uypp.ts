export const getUsers = async () => {
  const res = await fetch(`${process.env.BASE_URL}/api/users`);
  const { data } = await res.json();
  return data;
};
