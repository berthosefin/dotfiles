import Link from "next/link";

type TypeProps = {
  href: string;
  children: string;
};

export default function NavLink({ href, children }: TypeProps) {
  return <Link href={href}>{children}</Link>;
}
