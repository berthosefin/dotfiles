export const getUsers = async () => {
  const response = await fetch(`/api/users`);
  const data = await response.json();
  return data;
};

export async function createUser(formData: any) {
  try {
    const response = await fetch("/api/users", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(formData),
    });
    const data = await response.json();
    return data;
  } catch (error) {
    return error;
  }
}
