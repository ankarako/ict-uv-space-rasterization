import torch

def rasterize_triangle(v_pos: torch.Tensor, v_uvs: torch.Tensor, feats: torch.Tensor, output_tex: torch.Tensor) -> torch.Tensor:
    """
    Rasterize a triangle features.

    :param v_pos The triangle's vertex positions 3 x 3
    :param v_uvs The uv coordinates corresponding to the triangle'v vertices 3 x 2
    :param feats The features to rasterize 3 x d_{feat}
    :param output_tex The output texture
    :return The updated output texture
    """
    U, V = torch.meshgrid(
        torch.linspace(0, 1, output_tex.shape[0]).cuda(),
        torch.linspace(0, 1, output_tex.shape[1]).cuda(),
    indexing='ij')

    edge1 = v_uvs[1, :] - v_uvs[0, :]
    edge2 = v_uvs[2, :] - v_uvs[0, :]

    # determinant for bary-coords
    det = edge1[0] * edge2[1] - edge1[1] * edge2[0]

    # avoid div by 0
    if torch.abs(det) < 1.0e-8:
        return output_tex
    
    # transform the UV grid to the barycentric space of the triangle
    # for each pixel (U, V) calc the corresponding barycentric coords
    delta_u = U - v_uvs[0, 0]
    delta_v = V - v_uvs[0, 1]

    # bary coords
    w1 = (edge2[1] * delta_u - edge2[0] * delta_v) / det
    w2 = (edge1[0] * delta_v - edge1[1] * delta_u) / det
    w0 = 1 - w1 - w2

    # inside triangle pixel mask
    mask = (w0 >= 0) & (w1 >= 0) & (w2 >= 0)

    # interpolate features
    features = torch.zeros_like(output_tex)
    features[mask] = w0[mask][:, None] * feats[0, :] + w1[mask][:, None] * feats[1, :] + w2[mask][:, None] * feats[2, :]

    output_tex += features
    return output_tex