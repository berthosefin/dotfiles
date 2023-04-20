import { User } from "@prisma/client";

export async function createUser(formData: User) {
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

export async function getUsers() {
  const response = await fetch("/api/users");
  const data = await response.json();
  return data;
}

export async function getUserById(id: string) {
  const response = await fetch(`/api/users/${id}`);
  const data = await response.json();

  if (data) return data;
  return {};
}

export async function updateUser(id: string, formData: User) {
  const response = await fetch("/api/users", {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(formData),
  });
  const data = await response.json();
  return data;
}
