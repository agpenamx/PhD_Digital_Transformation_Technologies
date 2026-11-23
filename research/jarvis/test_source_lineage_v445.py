"""Synthetic tests only; neither external evidence nor a deployed agent test."""
import unittest
from source_lineage_v445 import source_roots, coordination_links


class LineageTests(unittest.TestCase):
    def test_root(self):
        self.assertEqual(source_roots({'s': ()}, 's'), frozenset({'s'}))

    def test_ten_agents_one_origin(self):
        graph = {'source': ()}
        graph.update({f'agent{i}': ('source',) for i in range(10)})
        graph['report'] = tuple(f'agent{i}' for i in range(10))
        self.assertEqual(len(source_roots(graph, 'report')), 1)

    def test_two_declared_origins(self):
        graph = {'s1': (), 's2': (), 'report': ('s1', 's2')}
        self.assertEqual(source_roots(graph, 'report'), frozenset({'s1', 's2'}))

    def test_duplicate_edge(self):
        self.assertEqual(source_roots({'s': (), 'a': ('s', 's')}, 'a'), frozenset({'s'}))

    def test_diamond(self):
        graph = {'s': (), 'a': ('s',), 'b': ('s',), 'c': ('a', 'b')}
        self.assertEqual(len(source_roots(graph, 'c')), 1)

    def test_cycle_rejected(self):
        with self.assertRaises(ValueError):
            source_roots({'a': ('b',), 'b': ('a',)}, 'a')

    def test_missing_parent_rejected(self):
        with self.assertRaises(ValueError):
            source_roots({'a': ('missing',)}, 'a')

    def test_unknown_node_rejected(self):
        with self.assertRaises(ValueError):
            source_roots({'s': ()}, 'missing')

    def test_strings_not_parent_collections(self):
        with self.assertRaises(ValueError):
            source_roots({'s': (), 'a': 's'}, 'a')

    def test_unrelated_cycle_rejected(self):
        with self.assertRaises(ValueError):
            source_roots({'s': (), 'loop': ('loop',)}, 's')

    def test_invalid_ids_rejected(self):
        with self.assertRaises(ValueError):
            source_roots({'s': (None,)}, 's')

    def test_long_chain(self):
        graph = {'s0': ()}
        graph.update({f's{i}': (f's{i-1}',) for i in range(1, 1501)})
        self.assertEqual(source_roots(graph, 's1500'), frozenset({'s0'}))

    def test_pair_count(self):
        self.assertEqual(coordination_links(5), 10)

    def test_zero_and_one_nodes(self):
        self.assertEqual(coordination_links(0), 0)
        self.assertEqual(coordination_links(1), 0)

    def test_invalid_counts(self):
        for value in (-1, True, 2.5, '3'):
            with self.subTest(value=value), self.assertRaises(ValueError):
                coordination_links(value)


if __name__ == '__main__':
    unittest.main()
