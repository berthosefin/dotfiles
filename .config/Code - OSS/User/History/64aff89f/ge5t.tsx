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
    <div className="grid sm:grid-cols-1 md:grid-cols-2 lg:gri-cols-4 gap-5 p-5">
      {techGroup.map((group: string, id: number) => (
        <Link
          className="shadow-gray-50 bg-gray-300 rounded text-xl text-center py-10 font-bold hover:bg-blue-500 hover:text-white"
          href={"/techGroup/${group}"}
          key={id}
        >
          {group}
        </Link>
      ))}
    </div>
  );
}
