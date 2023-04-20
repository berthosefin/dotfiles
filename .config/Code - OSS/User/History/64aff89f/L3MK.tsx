import Link from "next/link";
import React from "react";

const fetchTechGroup = async () => {
  const res = await fetch(
    "http://127.0.0.1:8090/api/collections/techGroup/records"
  );
  const data = await res.json();
  return data.items.map((item: { name: string }) => item.name);
};

export default async function techGroup() {
  const techGroup = await fetchTechGroup();
  return (
    <div>
      {techGroup.map((item: string) => (
        <Link href={"/"}></Link>
      ))}
    </div>
  );
}
