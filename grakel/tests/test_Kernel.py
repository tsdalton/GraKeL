"""A random input test for Kernel Oblects similar to test_estimator."""
import warnings
import numpy as np

from grakel.datasets import generate_dataset

from grakel import GraphKernel
from grakel.kernels import GraphletSampling
from grakel.kernels import RandomWalk
from grakel.kernels import RandomWalkLabeled
from grakel.kernels import ShortestPath
from grakel.kernels import ShortestPathAttr
from grakel.kernels import WeisfeilerLehman
from grakel.kernels import NeighborhoodHash
from grakel.kernels import PyramidMatch
from grakel.kernels import SubgraphMatching
from grakel.kernels import NeighborhoodSubgraphPairwiseDistance
from grakel.kernels import LovaszTheta
from grakel.kernels import SvmTheta
from grakel.kernels import OddSth
from grakel.kernels import Propagation
from grakel.kernels import PropagationAttr
from grakel.kernels import HadamardCode
from grakel.kernels import MultiscaleLaplacian
from grakel.kernels import MultiscaleLaplacianFast
from grakel.kernels import VertexHistogram
from grakel.kernels import EdgeHistogram
from grakel.kernels import GraphHopper
from grakel.kernels import CoreFramework

verbose, normalize = False, True
default_eigvalue_precision = float("-1e-5")
rs = np.random.RandomState(42)
warnings.filterwarnings("ignore")

cvxopt = True
try:
    import cvxopt
except ImportError:
    cvxopt = False


def test_random_walk():
    """Random input test for the Simple Random Walk kernel."""
    train, test = generate_dataset(n_graphs=100,
                                   r_vertices=(10, 20),
                                   r_connectivity=(0.4, 0.8),
                                   r_weight_edges=(0.01, 12.0),
                                   n_graphs_test=40,
                                   random_seed=rs,
                                   features=None)

    rw_kernel = RandomWalk(verbose=verbose, normalize=normalize)
    gk = GraphKernel(kernel={"name": "random_walk"}, verbose=verbose,
                     normalize=normalize)

    try:
        rw_kernel.fit_transform(train)
        rw_kernel.transform(test)
        gk.fit_transform(test)
        gk.transform(test)
        assert True
    except Exception as exception:
        assert False, exception


def test_random_walk_labels():
    """Random input test for the Labelled Random Walk kernel."""
    train, test = generate_dataset(n_graphs=100,
                                   r_vertices=(10, 20),
                                   r_connectivity=(0.4, 0.8),
                                   r_weight_edges=(0.01, 12.0),
                                   n_graphs_test=40,
                                   random_seed=rs,
                                   features=('nl', 3))

    rw_kernel = RandomWalkLabeled(verbose=verbose, normalize=normalize)
    gk = GraphKernel(kernel={"name": "random_walk", "with_labels": True},
                     verbose=verbose, normalize=normalize)

    try:
        rw_kernel.fit_transform(train)
        rw_kernel.transform(test)
        gk.fit_transform(test)
        gk.transform(test)
        assert True
    except Exception as exception:
        assert False, exception


def test_shortest_path():
    """Random input test for the Shortest Path kernel."""
    train, test = generate_dataset(n_graphs=100,
                                   r_vertices=(10, 20),
                                   r_connectivity=(0.4, 0.8),
                                   r_weight_edges=(1, 1),
                                   n_graphs_test=40,
                                   random_seed=rs,
                                   features=('nl', 3))

    sp_kernel = ShortestPath(verbose=verbose, normalize=normalize)
    gk = GraphKernel(kernel={"name": "shortest_path"}, verbose=verbose,
                     normalize=normalize)

    try:
        sp_kernel.fit_transform(train)
        sp_kernel.transform(test)
        gk.fit_transform(test)
        gk.transform(test)
        assert True
    except Exception as exception:
        assert False, exception

    train, test = generate_dataset(n_graphs=50,
                                   r_vertices=(5, 10),
                                   r_connectivity=(0.4, 0.8),
                                   r_weight_edges=(1, 1),
                                   n_graphs_test=20,
                                   random_seed=rs,
                                   features=('na', 5))

    sp_kernel = ShortestPathAttr(verbose=verbose, normalize=normalize)
    gk = GraphKernel(kernel={"name": "shortest_path", "as_attributes": True},
                     verbose=verbose, normalize=normalize)

    try:
        sp_kernel.fit_transform(train)
        sp_kernel.transform(test)
        gk.fit_transform(test)
        gk.transform(test)
        assert True
    except Exception as exception:
        assert False, exception


def test_graphlet_sampling():
    """Random input test for the Graphlet Sampling Kernel."""
    train, test = generate_dataset(n_graphs=100,
                                   r_vertices=(10, 20),
                                   r_connectivity=(0.4, 0.8),
                                   r_weight_edges=(1, 1),
                                   n_graphs_test=40,
                                   random_seed=rs,
                                   features=('nl', 3))

    gs_kernel = GraphletSampling(verbose=verbose, normalize=normalize, sampling=dict(n_samples=50))
    gk = GraphKernel(kernel={"name": "graphlet_sampling",
                             "sampling": {"n_samples": 50}},
                     verbose=verbose, normalize=normalize)

    try:
        gs_kernel.fit_transform(train)
        gs_kernel.transform(test)
        gk.fit_transform(train)
        gk.transform(test)
        assert True
    except Exception as exception:
        assert False, exception


def test_weisfeiler_lehman():
    """Random input test for the Weisfeiler Lehman kernel."""
    train, test = generate_dataset(n_graphs=100,
                                   r_vertices=(10, 20),
                                   r_connectivity=(0.4, 0.8),
                                   r_weight_edges=(1, 1),
                                   n_graphs_test=40,
                                   random_seed=rs,
                                   features=('nl', 3))

    wl_st_kernel = WeisfeilerLehman(verbose=verbose, normalize=normalize,
                                    base_kernel=VertexHistogram)
    gk = GraphKernel(kernel=[{"name": "weisfeiler_lehman"},
                     {"name": "vertex_histogram"}],
                     verbose=verbose, normalize=normalize)

    try:
        wl_st_kernel.fit_transform(train)
        wl_st_kernel.transform(test)
        gk.fit_transform(train)
        gk.transform(test)
        assert True
    except Exception as exception:
        assert False, exception


def test_pyramid_match():
    """Random input test for the Pyramid Match kernel."""
    train, test = generate_dataset(n_graphs=100,
                                   r_vertices=(10, 20),
                                   r_connectivity=(0.4, 0.8),
                                   r_weight_edges=(1, 1),
                                   n_graphs_test=40,
                                   random_seed=rs,
                                   features=('nl', 3))

    pm_kernel = PyramidMatch(verbose=verbose, normalize=normalize)
    gk = GraphKernel(kernel={"name": "pyramid_match"}, verbose=verbose,
                     normalize=normalize)

    try:
        pm_kernel.fit_transform(train)
        pm_kernel.transform(test)
        gk.fit_transform(train)
        gk.transform(test)
        assert True
    except Exception as exception:
        assert False, exception


def test_pyramid_match_no_labels():
    """Random input test for the Pyramid Match kernel with no labels."""
    train, test = generate_dataset(n_graphs=100,
                                   r_vertices=(10, 20),
                                   r_connectivity=(0.4, 0.8),
                                   r_weight_edges=(1, 1),
                                   n_graphs_test=40,
                                   random_seed=rs,
                                   features=None)

    pm_kernel = PyramidMatch(verbose=verbose, normalize=normalize, with_labels=False)
    gk = GraphKernel(kernel={"name": "pyramid_match", "with_labels": False},
                     verbose=verbose, normalize=normalize)

    try:
        pm_kernel.fit_transform(train)
        pm_kernel.transform(test)
        gk.fit_transform(train)
        gk.transform(test)
        assert True
    except Exception as exception:
        assert False, exception


def test_neighborhood_hash():
    """Random input test for the Neighborhood Hash kernel."""
    train, test = generate_dataset(n_graphs=100,
                                   r_vertices=(10, 20),
                                   r_connectivity=(0.4, 0.8),
                                   r_weight_edges=(1, 1),
                                   n_graphs_test=40,
                                   random_seed=rs,
                                   features=('nl', 3))

    nh_kernel = NeighborhoodHash(verbose=verbose, normalize=normalize)
    gk = GraphKernel(kernel={"name": "neighborhood_hash"}, verbose=verbose,
                     normalize=normalize)

    try:
        nh_kernel.fit_transform(train)
        nh_kernel.transform(test)
        gk.fit_transform(train)
        gk.transform(test)
        assert True
    except Exception as exception:
        assert False, exception


def test_subgraph_matching():
    """Random input test for the Subgraph Matching kernel."""
    # node-label/edge-label
    train, test = generate_dataset(n_graphs=100,
                                   r_vertices=(10, 20),
                                   r_connectivity=(0.4, 0.8),
                                   r_weight_edges=(1, 1),
                                   n_graphs_test=40,
                                   random_seed=rs,
                                   features=('nl', 3, 'el', 4))

    sm_kernel = SubgraphMatching(verbose=verbose, normalize=normalize)
    gk = GraphKernel(kernel={"name": "subgraph_matching"}, verbose=verbose,
                     normalize=normalize)

    try:
        sm_kernel.fit_transform(train)
        sm_kernel.transform(test)
        gk.fit_transform(train)
        gk.transform(test)
        assert True
    except Exception as exception:
        assert False, exception

    # node-label/edge-attribute
    train, test = generate_dataset(n_graphs=50,
                                   r_vertices=(5, 10),
                                   r_connectivity=(0.4, 0.8),
                                   r_weight_edges=(1, 1),
                                   n_graphs_test=20,
                                   random_seed=rs,
                                   features=('nl', 3, 'ea', 5))

    sm_kernel = SubgraphMatching(verbose=verbose, normalize=normalize, ke=np.dot)
    gk = GraphKernel(kernel={"name": "subgraph_matching", "ke": np.dot},
                     verbose=verbose, normalize=normalize)

    try:
        sm_kernel.fit_transform(train)
        sm_kernel.transform(test)
        gk.fit_transform(train)
        gk.transform(test)
        assert True
    except Exception as exception:
        assert False, exception

    # node-attribute/edge-label
    train, test = generate_dataset(n_graphs=50,
                                   r_vertices=(5, 10),
                                   r_connectivity=(0.4, 0.8),
                                   r_weight_edges=(1, 1),
                                   n_graphs_test=20,
                                   random_seed=rs,
                                   features=('na', 4, 'el', 3))

    sm_kernel = SubgraphMatching(verbose=verbose, normalize=normalize, kv=np.dot)
    gk = GraphKernel(kernel={"name": "subgraph_matching", "kv": np.dot},
                     verbose=verbose, normalize=normalize)

    try:
        sm_kernel.fit_transform(train)
        sm_kernel.transform(test)
        gk.fit_transform(train)
        gk.transform(test)
        assert True
    except Exception as exception:
        assert False, exception

    # node-attribute/edge-attribute
    train, test = generate_dataset(n_graphs=50,
                                   r_vertices=(5, 10),
                                   r_connectivity=(0.4, 0.8),
                                   r_weight_edges=(1, 1),
                                   n_graphs_test=20,
                                   random_seed=rs,
                                   features=('na', 4, 'ea', 6))

    sm_kernel = SubgraphMatching(verbose=verbose, normalize=normalize, ke=np.dot, kv=np.dot)
    gk = GraphKernel(kernel={"name": "subgraph_matching", "kv": np.dot, "ke": np.dot},
                     verbose=verbose, normalize=normalize)

    try:
        sm_kernel.fit_transform(train)
        sm_kernel.transform(test)
        gk.fit_transform(train)
        gk.transform(test)
        assert True
    except Exception as exception:
        assert False, exception


def test_neighborhood_subgraph_pairwise_distance():
    """Random input test for the Neighborhood Subgraph Pairwise Distance kernel."""
    train, test = generate_dataset(n_graphs=100,
                                   r_vertices=(5, 10),
                                   r_connectivity=(0.4, 0.8),
                                   r_weight_edges=(1, 1),
                                   n_graphs_test=40,
                                   random_seed=rs,
                                   features=('nl', 5, 'el', 4))

    nspd_kernel = NeighborhoodSubgraphPairwiseDistance(verbose=verbose, normalize=normalize)
    gk = GraphKernel(kernel={
        "name": "neighborhood_subgraph_pairwise_distance"},
                     verbose=verbose, normalize=normalize)

    try:
        nspd_kernel.fit_transform(train)
        nspd_kernel.transform(test)
        gk.fit_transform(train)
        gk.transform(test)
        assert True
    except Exception as exception:
        assert False, exception


if cvxopt:
    def test_lovasz_theta():
        """Random input test for the Lovasz-theta distance kernel."""
        train, test = generate_dataset(n_graphs=50,
                                       r_vertices=(5, 10),
                                       r_connectivity=(0.4, 0.8),
                                       r_weight_edges=(1, 1),
                                       n_graphs_test=20,
                                       random_seed=rs,
                                       features=None)

        lt_kernel = LovaszTheta(verbose=verbose, normalize=normalize)
        gk = GraphKernel(kernel={"name": "lovasz_theta"},
                         verbose=verbose, normalize=normalize)

        try:
            lt_kernel.fit_transform(train)
            lt_kernel.transform(test)
            gk.fit_transform(train)
            gk.transform(test)
            assert True
        except Exception as exception:
            assert False, exception


def test_svm_theta():
    """Random input test for the SVM-theta distance kernel."""
    train, test = generate_dataset(n_graphs=100,
                                   r_vertices=(10, 20),
                                   r_connectivity=(0.4, 0.8),
                                   r_weight_edges=(1, 1),
                                   n_graphs_test=40,
                                   random_seed=rs,
                                   features=None)

    svm_kernel = SvmTheta(verbose=verbose, normalize=normalize)
    gk = GraphKernel(kernel={"name": "svm_theta"},
                     verbose=verbose, normalize=normalize)

    try:
        svm_kernel.fit_transform(train)
        svm_kernel.transform(test)
        gk.fit_transform(train)
        gk.transform(test)
        assert True
    except Exception as exception:
        assert False, exception


def test_odd_sth():
    """Random input test for the ODD-STh kernel."""
    train, test = generate_dataset(n_graphs=100,
                                   r_vertices=(10, 20),
                                   r_connectivity=(0.4, 0.8),
                                   r_weight_edges=(1, 1),
                                   n_graphs_test=40,
                                   random_seed=rs,
                                   features=('nl', 4))

    odd_sth_kernel = OddSth(verbose=verbose, normalize=normalize)
    gk = GraphKernel(kernel={"name": "odd_sth"},
                     verbose=verbose, normalize=normalize)

    try:
        odd_sth_kernel.fit_transform(train)
        odd_sth_kernel.transform(test)
        gk.fit_transform(train)
        gk.transform(test)
        assert True
    except Exception as exception:
        assert False, exception


def test_propagation():
    """Random input test for the Propagation kernel."""
    train, test = generate_dataset(n_graphs=100,
                                   r_vertices=(10, 20),
                                   r_connectivity=(0.4, 0.8),
                                   r_weight_edges=(float("1e-5"), 10),
                                   n_graphs_test=40,
                                   random_seed=rs,
                                   features=('nl', 4))

    propagation_kernel = Propagation(verbose=verbose, normalize=normalize)
    gk = GraphKernel(kernel={"name": "propagation"},
                     verbose=verbose, normalize=normalize)

    try:
        propagation_kernel.fit_transform(train)
        propagation_kernel.transform(test)
        gk.fit_transform(train)
        gk.transform(test)
        assert True
    except Exception as exception:
        assert False, exception

    train, test = generate_dataset(n_graphs=100,
                                   r_vertices=(10, 20),
                                   r_connectivity=(0.4, 0.8),
                                   r_weight_edges=(float("1e-5"), 10),
                                   n_graphs_test=40,
                                   random_seed=rs,
                                   features=('na', 5))

    propagation_kernel_attr = PropagationAttr(verbose=verbose, normalize=normalize)
    gk = GraphKernel(kernel={"name": "propagation", "with_attributes": True},
                     verbose=verbose, normalize=normalize)

    try:
        propagation_kernel_attr.fit_transform(train)
        propagation_kernel_attr.transform(test)
        gk.fit_transform(train)
        gk.transform(test)
        assert True
    except Exception as exception:
        assert False, exception


def test_hadamard_code():
    """Random input test for the Hadamard Code kernel."""
    train, test = generate_dataset(n_graphs=100,
                                   r_vertices=(10, 20),
                                   r_connectivity=(0.4, 0.8),
                                   r_weight_edges=(1, 1),
                                   n_graphs_test=40,
                                   random_seed=rs,
                                   features=('nl', 5))

    hadamard_code_kernel = HadamardCode(verbose=verbose, normalize=normalize,
                                        base_kernel=VertexHistogram)
    gk = GraphKernel(kernel=[{"name": "hadamard_code"},
                             {"name": "subtree_wl"}],
                     verbose=verbose, normalize=normalize)

    try:
        hadamard_code_kernel.fit_transform(train)
        hadamard_code_kernel.transform(test)
        gk.fit_transform(train)
        gk.transform(test)
        assert True
    except Exception as exception:
        assert False, exception


def test_multiscale_laplacian():
    """Random input test for the Multiscale Laplacian kernel."""
    # Intialise kernel
    train, test = generate_dataset(n_graphs=30,
                                   r_vertices=(5, 10),
                                   r_connectivity=(0.4, 0.8),
                                   r_weight_edges=(1, 1),
                                   n_graphs_test=10,
                                   random_seed=rs,
                                   features=('na', 5))

    ml_kernel = MultiscaleLaplacian(verbose=verbose, normalize=normalize)
    gk = GraphKernel(kernel={"name": "multiscale_laplacian"},
                     verbose=verbose, normalize=normalize)

    try:
        ml_kernel.fit_transform(train)
        ml_kernel.transform(test)
        gk.fit_transform(train)
        gk.transform(test)
        assert True
    except Exception as exception:
        assert False, exception


def test_multiscale_laplacian_fast():
    """Random input test for the Fast Multiscale Laplacian kernel."""
    # Initialise kernel
    train, test = generate_dataset(n_graphs=100,
                                   r_vertices=(10, 20),
                                   r_connectivity=(0.4, 0.8),
                                   r_weight_edges=(1, 1),
                                   n_graphs_test=40,
                                   random_seed=rs,
                                   features=('na', 5))

    mlf_kernel = MultiscaleLaplacianFast(verbose=verbose, normalize=normalize)
    gk = GraphKernel(kernel={"name": "multiscale_laplacian", "which": "fast"},
                     verbose=verbose, normalize=normalize)

    try:
        mlf_kernel.fit_transform(train)
        mlf_kernel.transform(test)
        gk.fit_transform(train)
        gk.transform(test)
        assert True
    except Exception as exception:
        assert False, exception


def test_vertex_histogram():
    """Random input test for the Vertex Histogram Kernel."""
    train, test = generate_dataset(n_graphs=100,
                                   r_vertices=(10, 20),
                                   r_connectivity=(0.4, 0.8),
                                   r_weight_edges=(1, 1),
                                   n_graphs_test=40,
                                   random_seed=rs,
                                   features=('nl', 5))

    vh_kernel = VertexHistogram(verbose=verbose, normalize=normalize)
    gk = GraphKernel(kernel={"name": "vertex_histogram"},
                     verbose=verbose, normalize=normalize)

    try:
        vh_kernel.fit_transform(train)
        vh_kernel.transform(test)
        gk.fit_transform(train)
        gk.transform(test)
        assert True
    except Exception as exception:
        assert False, exception


def test_edge_histogram():
    """Random input test for the Edge Histogram kernel."""
    train, test = generate_dataset(n_graphs=100,
                                   r_vertices=(10, 20),
                                   r_connectivity=(0.4, 0.8),
                                   r_weight_edges=(1, 1),
                                   n_graphs_test=40,
                                   random_seed=rs,
                                   features=('el', 4))

    eh_kernel = EdgeHistogram(verbose=verbose, normalize=normalize)
    gk = GraphKernel(kernel={"name": "edge_histogram"},
                     verbose=verbose, normalize=normalize)

    try:
        eh_kernel.fit_transform(train)
        eh_kernel.transform(test)
        gk.fit_transform(train)
        gk.transform(test)
        assert True
    except Exception as exception:
        assert False, exception


def test_graph_hopper():
    """Random input test for the Graph Hopper kernel."""
    train, test = generate_dataset(n_graphs=100,
                                   r_vertices=(10, 20),
                                   r_connectivity=(0.4, 0.8),
                                   r_weight_edges=(1, 1),
                                   n_graphs_test=40,
                                   random_seed=rs,
                                   features=('na', 4))

    gh_kernel = GraphHopper(verbose=verbose, normalize=normalize)
    gk = GraphKernel(kernel={"name": "graph_hopper"},
                     verbose=verbose, normalize=normalize)

    try:
        gh_kernel.fit_transform(train)
        gh_kernel.transform(test)
        gk.fit_transform(train)
        gk.transform(test)
        assert True
    except Exception as exception:
        assert False, exception


def test_core_framework():
    """Random input test for the Core kernel Framework."""
    train, test = generate_dataset(n_graphs=100,
                                   r_vertices=(10, 20),
                                   r_connectivity=(0.4, 0.8),
                                   r_weight_edges=(1, 1),
                                   n_graphs_test=40,
                                   random_seed=rs,
                                   features=('nl', 4))

    base_kernel = (WeisfeilerLehman, dict(base_kernel=VertexHistogram))
    core_framework = CoreFramework(verbose=verbose, normalize=normalize, base_kernel=base_kernel)

    kernel = [{"name": "core_framework"}, {"name": "weisfeiler_lehman"}, {"name": "vertex_histogram"}]
    gk = GraphKernel(kernel=kernel, verbose=verbose, normalize=normalize)
    try:
        core_framework.fit_transform(train)
        core_framework.transform(test)
        gk.fit_transform(train)
        gk.transform(test)
        assert True
    except Exception as exception:
        assert False, exception


if __name__ == "__main__":
    warnings.filterwarnings("once")
    verbose = True

    test_random_walk()
    test_random_walk_labels()
    test_shortest_path()
    test_graphlet_sampling()
    test_weisfeiler_lehman()
    test_pyramid_match()
    test_pyramid_match_no_labels()
    test_neighborhood_hash()
    test_subgraph_matching()
    test_neighborhood_subgraph_pairwise_distance()
    test_lovasz_theta()
    test_svm_theta()
    test_odd_sth()
    test_propagation()
    test_hadamard_code()
    test_multiscale_laplacian()
    test_multiscale_laplacian_fast()
    test_vertex_histogram()
    test_edge_histogram()
    test_graph_hopper()
    test_core_framework()
