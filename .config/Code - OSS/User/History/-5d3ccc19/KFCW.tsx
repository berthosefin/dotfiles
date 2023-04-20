import React from "react";
import TechList from "@/components/TechList";

const fetchTech = async (group: string) => {
  const res = await fetch(`http://127.0.0.1:8090/api/collections/tech/records`);
  res.items.map((item) => {
    item.techGroupName = { group };
  });
  const response = res.json();
  return response;
};

type TypeProps = {
  params: {
    group: string;
  };
};

export default async function page({ params }: TypeProps) {
  const techlist = await fetchTech(params.group);
  console.log(techlist.items);
  return <TechList techlist={techlist.items} group={params.group} />;
}
