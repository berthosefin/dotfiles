import Link from "next/link";
import React from "react";

const fetchTechGroup = async () => {
  const res = await fetch(
    "http://127.0.0.1:8090/api/collections/techGroup/records"
  );
  const response = await res.json();
  return response.items.map((item: { name: string }) => item.name);
};

export default async function techGroup() {
  const techGroup = await fetchTechGroup();
  return (
    <div className="grid sm:grid-cols-1 md:grid-cols-2 lg:gri-cols-4 gap-5 p-5">
      {techGroup.map((group: string, id: number) => (
        <Link
          className="shadow-gray-500 bg-[#D8DEE9] rounded text-xl text-center py-10 font-bold hover:bg-[#4C566A] hover:text-[#D8DEE9]"
          href={`/techGroup/${group}`}
          key={id}
        >
          {group.toLocaleUpperCase()}
        </Link>
      ))}
    </div>
  );
}
