// e.g. in `pages/index.tsx`
import { prisma } from "./db";

export const getServerSideProps = async ({ req }) => {
  const token = req.headers.AUTHORIZATION;
  const userId = await getUserId(token);
  const posts = await prisma.post.findMany({
    where: {
      author: { id: userId },
    },
  });
  return { props: { posts } };
};
("");
