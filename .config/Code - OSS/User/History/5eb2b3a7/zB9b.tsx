import React from "react";
import Image from "next/image";

type TypeProps = {
  techlist: [
    collectionId: "e1uj1s6fskpw296",
    collectionName: "tech",
    created: "2023-02-13 08:39:20.366Z",
    detail: "aut est omnis dolores\\nneque rerum quod ea rerum velit pariatur beatae excepturi\\net provident voluptas corrupti\\ncorporis harum reprehenderit dolores eligendi",
    id: "2sh6q032nr6upgk",
    logo: "git_zaQM4GXeAU.png",
    name: "git",
    techGroupName: "bbrfvz3vrb01ki3",
    updated: "2023-02-13 08:39:20.366Z"
  ];
  group: string;
};

export default function TechList({ techlist, group }: TypeProps) {
  return (
    <div className="grid sm:grid-cols-1 md:grid-cols-2 lg:gri-cols-4 gap-5 p-5">
      {techlist.map((tech, id: number) => {
        return (
          <div key="id" className="rounded bg-slate-300">
            <Image
              src={techlist.logo}
              width={500}
              height={500}
              alt={`logo: ${techlist.name}`}
            />
          </div>
        );
      })}
    </div>
  );
}
