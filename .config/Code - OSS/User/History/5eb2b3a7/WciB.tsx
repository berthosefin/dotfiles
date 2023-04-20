import React from "react";
import Image from "next/image";

type TypeProps = {
  techlist: [
    {
      logo: string;
      name: string;
    }
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
